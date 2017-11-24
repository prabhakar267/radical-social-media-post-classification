import os

from constants import DATA_DIR, TWEETS_DUMP_DIR, DEFAULT_HASHTAG_SCORE, NEW_HASHTAGS_DISCOVERY_RATE
import utils as u


total_tweet_count = 0
visited_tweets = []
hashtags_frequency = {}
tweet_ctr = 0

tweets_dump_path = os.path.join(DATA_DIR, TWEETS_DUMP_DIR)

for dp, dn, filenames in os.walk(tweets_dump_path):
    total_tweet_count += len(filenames)

    for tweet_file in filenames:
        tweet_id = tweet_file  # filename is tweet id itself
        tweet_filepath = os.path.join(dp, tweet_id)

        if tweet_id not in visited_tweets:
            visited_tweets.append(tweet_id)
            tweet_hashtags = u.get_list_of_hashtags(tweet_filepath)

            for hashtag in tweet_hashtags:
                hashtag_string = hashtag['text']
                hashtags_frequency = u.increase_frequency(hashtags_frequency, 
                                                          hashtag_string,
                                                          DEFAULT_HASHTAG_SCORE)

            tweet_ctr += 1
            if tweet_ctr % 1000 == 0:
                print "INFO: {0} unique tweets out of {1} total found".format(tweet_ctr, total_tweet_count)


top_hashtags = sorted(hashtags_frequency, key=hashtags_frequency.get, reverse=True)
top_hashtags = top_hashtags[:NEW_HASHTAGS_DISCOVERY_RATE] 

print "Total tweets extracted: {}".format(total_tweet_count)
print "Total unique tweets found: {}".format(tweet_ctr)

for hashtag in top_hashtags:
    occurence_percentage = float(hashtags_frequency[hashtag]) / tweet_ctr * 100
    clean_hashtag_string = hashtag.encode('utf-8').strip()
    print "{0:.4f} | {1}s".format(occurence_percentage, clean_hashtag_string)
