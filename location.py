import os
import json

mypath = "Real"
total_count = 0
ctr = 0
location_tweets = 0

hashtags = {}
visited_tweets = []

for dp, dn, filenames in os.walk(mypath):
    total_count += len(filenames)
    for f in filenames:

        file_path = os.path.join(dp, f)
        if f not in visited_tweets:
            visited_tweets.append(f)
            with open(file_path) as data_file:    
                data = json.load(data_file)
                if data['geo']:
                    location_tweets += 1
            
            ctr += 1
            if ctr % 100 == 0:
                print ctr, '/', total_count

print "Total tweets extracted: " , total_count
print "Total unique tweets: " , ctr
print "Total unique tweets with location: " , location_tweets
