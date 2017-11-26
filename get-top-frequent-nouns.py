import os
import enchant
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

from constants import DATA_DIR, TWEETS_DUMP_DIR, NOUN_POS_TAGS, DEFAULT_NOUN_SCORE, \
                      NOUN_FREQUENCY_FP, NOUN_FREQUENCY_CLIP_LENGTH, MINIMUM_WORD_LENGTH
import utils as u


enchant_dictionary = enchant.Dict("en_US")
lmtzr = WordNetLemmatizer()


visited_tweets = []
text_feature_candidates = {}
total_tweet_count = 0
tweet_ctr = 0

tweets_dump_path = os.path.join(DATA_DIR, TWEETS_DUMP_DIR)

for dp, dn, filenames in os.walk(tweets_dump_path):
    total_tweet_count += len(filenames)
    
    for tweet_file in filenames:
        tweet_id = tweet_file  # filename is tweet id itself
        tweet_filepath = os.path.join(dp, tweet_id)

        if tweet_id not in visited_tweets:
            visited_tweets.append(tweet_id)
            tweet_string = u.get_tweet_text(tweet_filepath)
            clean_tweet_string = u.remove_hashtags(tweet_string)

            tokens = nltk.word_tokenize(clean_tweet_string)
            pos_tag_data = nltk.pos_tag(tokens)

            for token_tuple in pos_tag_data:
                noun_word = token_tuple[0]
                pos_tag = token_tuple[1] 
                if pos_tag in NOUN_POS_TAGS and enchant_dictionary.check(noun_word):
                    lemmatized_word = lmtzr.lemmatize(noun_word)
                    if len(lemmatized_word) > MINIMUM_WORD_LENGTH:
                        text_feature_candidates = u.increase_frequency(text_feature_candidates,
                                                                   lemmatized_word,
                                                                   DEFAULT_NOUN_SCORE)

        tweet_ctr += 1
        if tweet_ctr % 1000 == 0:
            print "INFO: {0} tweets checked out of {1} total found".format(tweet_ctr, total_tweet_count)

print "Total tweets checked: {}".format(tweet_ctr)

noun_frequency_filepath = os.path.join(DATA_DIR, NOUN_FREQUENCY_FP)
u.store_json_response(noun_frequency_filepath, text_feature_candidates)

noun_occurence_frequency = sorted(text_feature_candidates, key=text_feature_candidates.get, reverse=True)
noun_occurence_frequency = noun_occurence_frequency[:NOUN_FREQUENCY_CLIP_LENGTH]

for noun_word in reversed(noun_occurence_frequency):
    occurence_percentage = float(text_feature_candidates[noun_word]) / tweet_ctr * 100
    print "{0:.4f} | {1}".format(occurence_percentage, noun_word)


