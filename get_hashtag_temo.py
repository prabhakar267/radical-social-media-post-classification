import json
import os
import sys

def increase_score(score_dict, key, value):
    if key in score_dict:
        score_dict[key] += value
    else:
        score_dict[key] = value

    return score_dict


def get_history(directory_name, number_of_tweets):
    history_file = meta_path + "/" + directory_name
    empty_dict = {}

    if os.path.exists(history_file):
        with open(history_file) as data_file:
            data = json.load(data_file)
            history_tweets_count = data['count']

            if history_tweets_count == number_of_tweets:
                return data['tweets']
            else:

    return


def add_hashtag(hashtags, hashtag_text, score):
    if(len(sys.argv) > 1):
        clean_hashtag = hashtag_text.lower()
    else:
        clean_hashtag = hashtag_text

    hashtags = increase_score(hashtags, clean_hashtag, score)
    return hashtags


def merge_


data_path = "Real"
meta_path = "meta"
total_count = 0
ctr = 0

hashtags = {}
visited_tweets = []

for dp, dn, filenames in os.walk(data_path):
    total_count += len(filenames)
    if len(filenames):
        directory_name = dp.split(os.path.sep)[-1]
        old_tweets = get_history(directory_name, len(filenames))
        if old_tweets:
            for tweet in old_tweets.keys():
                hashtags = add_hashtag(hashtags, tweet, old_tweets[tweet])
    else:
        for f in filenames:
            if ctr % 100 == 0:
                print ctr, '/', total_count

            file_path = os.path.join(dp, f)
            if f not in visited_tweets:
                visited_tweets.append(f)
                with open(file_path) as data_file:    
                    data = json.load(data_file)
                    hashtags_list = data['entities']['hashtags']
                    for hashtag in hashtags_list:
                        hashtags = add_hashtag(hashtags, hashtag['text'], 1)

                ctr += 1


sorted_list = sorted(hashtags, key=hashtags.get, reverse=True)
sorted_list = sorted_list[:20]

print "Total tweets extracted: " , total_count
print "Total unique tweets: " , ctr

for w in sorted_list:
    per = float(hashtags[w]) / ctr * 100
    print hashtags[w], '\t', per, '\t', w