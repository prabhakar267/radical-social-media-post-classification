import nltk
from nltk.stem.wordnet import WordNetLemmatizer

import json
import os
import sys
import enchant
from stop_words import get_stop_words

from utils import remove_hashtags


# nltk.data.path.append("nltk_data/")
enchant_dictionary = enchant.Dict("en_US")


def increase_score(score_dict, key, value):
    if key in score_dict:
        score_dict[key] += value
    else:
        score_dict[key] = value

    return score_dict


# mypath = "../Real"
file_path = "clean_tweets.json"
PROPER_NOUN_POS_TAGS = "NN NNS NNP NNPS".split(' ')
lmtzr = WordNetLemmatizer()
stop_words = get_stop_words('en')
ctr = 0

text_feature_candidates = {}
clean_tweets = []
visited_tweets = []

with open(file_path) as data_file:    
    data = json.load(data_file)
    total_count = len(data)

    for tweet in data:
        tokens = nltk.word_tokenize(tweet)
        pos_tag_data = nltk.pos_tag(tokens)
        # words = tweet.split()
        # for word in words:
        #     if enchant_dictionary.check(word) and len(word) > 2:
        #         if word not in stop_words:
        #             increase_score(text_feature_candidates, word, 1)


        for token_tuple in pos_tag_data:
            noun_word = token_tuple[0]
            # clean_noun_word = ''.join(e for e in noun_word if e.isalnum())
            clean_noun_word = noun_word
            # check if the "clean_noun_word" is not an empty string
            if clean_noun_word:
                if token_tuple[1] in PROPER_NOUN_POS_TAGS and enchant_dictionary.check(clean_noun_word):
                    lemmatized_word = lmtzr.lemmatize(clean_noun_word)
                    
                    if len(lemmatized_word) > 2:
                        text_feature_candidates = increase_score(text_feature_candidates, lemmatized_word, 1)

                        # existing_dict = increase_score(existing_dict, lemmatized_word, 1)


        ctr += 1
        if ctr % 100 == 0:
            print ctr, '/', total_count



# saving data
with open('tweet_features.json', 'w') as outfile:
    json.dump(text_feature_candidates, outfile)



sorted_list = sorted(text_feature_candidates, key=text_feature_candidates.get, reverse=True)
sorted_list = sorted_list[:40]

# print "Total tweets extracted: " , total_count
# print "Total unique tweets: " , ctr

for w in sorted_list:
    per = float(text_feature_candidates[w]) / ctr * 100
    print text_feature_candidates[w], '\t', per, '\t', w