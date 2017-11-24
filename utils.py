import sys
import os
import json

from TwitterAPI import TwitterAPI
from TwitterConstants import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET

from constants import DATA_DIR, HASHTAG_LIST_FILE


def get_twitter_client():
    client = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)
    return client


def load_search_hashtags():
    search_hashtags = list()
    filepath = os.path.join(DATA_DIR, HASHTAG_LIST_FILE)
    try:
        with open(filepath, "rb") as f:
            search_hashtags = f.readlines()
    except IOError as e:
        print "Invalid File Path at {}".format(filepath)
        sys.exit(1)
    
    # clean list
    search_hashtags = map(str.strip, search_hashtags)
    return search_hashtags


def write_tweet(output_filepath, tweet_json):
    try:
        with open(output_filepath, 'w+') as f:
            json.dump(tweet_json, f)
    except IOError as e:
        print "Output Directory doesnot exist"
        sys.exit(1)


def get_list_of_hashtags(tweet_filepath):
    hashtags_found = []
    try:
        with open(tweet_filepath) as f:    
            tweet_json = json.load(f)
            hashtags_found = tweet_json['entities']['hashtags']
    except IOError as e:
        print "Invalid File Path at {}".format(tweet_filepath)

    return hashtags_found


def increase_frequency(dictonary, key, increase):
    if key in dictonary:
        dictonary[key] += increase
    else:
        dictonary[key] = increase

    return dictonary