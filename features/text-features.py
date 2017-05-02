# import nltk
import json
import os
import sys

from utils import remove_hashtags


# nltk.data.path.append("nltk_data/")



def increase_score(score_dict, key, value):
    if key in score_dict:
        score_dict[key] += value
    else:
        score_dict[key] = value

    return score_dict


mypath = "../Real"
total_count = 0
ctr = 0

hashtags = {}
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
                # print json.dumps(data, indent=4, sort_keys=True)
                # print data['text']
                clean_tweet_text = remove_hashtags(data['text'])
                clean_tweets.append(clean_tweet_text)
                # tokens = nltk.word_tokenize(clean_tweet_text)

                # print tokens


            #     hashtags_list = data['entities']['hashtags']
            #     for hashtag in hashtags_list:
            #         if(len(sys.argv) > 1):
            #             clean_hashtag = hashtag['text'].lower()
            #         else:
            #             clean_hashtag = hashtag['text']

            #         hashtags = increase_score(hashtags, clean_hashtag, 1)
            ctr += 1
            if ctr % 100 == 0:
                # print clean_tweets
                # sys.exit()
                print ctr, '/', total_count

with open('clean_tweets.json', 'w') as outfile:
    json.dump(clean_tweets, outfile)

# sorted_list = sorted(hashtags, key=hashtags.get, reverse=True)
# sorted_list = sorted_list[:40]

# print "Total tweets extracted: " , total_count
# print "Total unique tweets: " , ctr

# for w in sorted_list:
#     per = float(hashtags[w]) / ctr * 100
#     print hashtags[w], '\t', per, '\t', w