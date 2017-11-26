import sys
import os
import json
import re

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


def get_tweet_text(tweet_filepath):
    tweet_text = ''
    try:
        with open(tweet_filepath) as f:    
            tweet_json = json.load(f)
            tweet_text = tweet_json['text']
    except IOError as e:
        print "Invalid File Path at {}".format(tweet_filepath)

    return tweet_text


def store_json_response(filepath, dictonary, beautify_mode=True):
    with open(filepath, 'w+') as f:
        if beautify_mode:
            json.dump(dictonary, f, sort_keys=True, indent=4)
        else:
            json.dump(dictonary, f)


def increase_frequency(dictonary, key, increase):
    if key in dictonary:
        dictonary[key] += increase
    else:
        dictonary[key] = increase

    return dictonary


def remove_hashtags(tweet):
    clean_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split())
    return clean_tweet