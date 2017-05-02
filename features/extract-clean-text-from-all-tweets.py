import json
import os

from utils import remove_hashtags

mypath = "../Real"
total_count = 0
ctr = 0

clean_tweets = []
visited_tweets = []

for dp, dn, filenames in os.walk(mypath):
    total_count += len(filenames)
    for f in filenames:

        file_path = os.path.join(dp, f)
        if f not in visited_tweets:
            visited_tweets.append(f)
            with open(file_path) as data_file:    
                data = json.load(data_file)

                clean_tweet_text = remove_hashtags(data['text'])
                clean_tweets.append(clean_tweet_text)

            ctr += 1
            if ctr % 100 == 0:
                print ctr, '/', total_count

with open('clean_tweets.json', 'w') as outfile:
    json.dump(clean_tweets, outfile)
