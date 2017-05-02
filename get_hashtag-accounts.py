import json
import os
import sys

def increase_score(score_dict, key, value):
    if key in score_dict:
        score_dict[key] += value
    else:
        score_dict[key] = value

    return score_dict


mypath = "tweets-accounts"
total_count = 0
ctr = 0

usernames = []


with open("accounts") as f:
    accounts = f.readlines()


accounts = map(str.strip, accounts)


for dp, dn, filenames in os.walk(mypath):
    total_count += len(filenames)
    for f in filenames:
        print ctr, '/', total_count

        file_path = os.path.join(dp, f)

        with open(file_path) as data_file:    
            data = json.load(data_file)
            # hashtags_list = data['entities']['hashtags']
            user_mentions_list = data['entities']['user_mentions']
            for i in user_mentions_list:
                screen_name = i['screen_name']
                if screen_name not in accounts:
                    usernames.append(screen_name)
                # print json.dumps(data, indent=4, sort_keys=True)
                # exit()
            # print data
            # for hashtag in hashtags_list:
            #     if(len(sys.argv) > 1):
            #         clean_hashtag = hashtag['text'].lower()
            #     else:
            #         clean_hashtag = hashtag['text']

                # hashtags = increase_score(hashtags, clean_hashtag, 1)
        ctr += 1
        # print ctr, f


for i in usernames:
    print i
# print usernames

# sorted_list = sorted(hashtags, key=hashtags.get, reverse=True)
# sorted_list = sorted_list[:20]

# print "Total tweets extracted: " , total_count
# print "Total unique tweets: " , ctr

# for w in sorted_list:
#     print hashtags[w], '\t', w