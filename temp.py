import os
import shutil

mypath = "train-data/dataset/GameOfThrones"
final_destination = "../radicalization-TT-dataset/TT-TEST"
total_count = 0
ctr = 0

hashtags = {}
visited_tweets = []

for dp, dn, filenames in os.walk(mypath):
    total_count += len(filenames)
    for f in filenames:

        file_path = os.path.join(dp, f)
        shutil.copy(file_path, final_destination)

        ctr += 1
    print ctr


# sorted_list = sorted(hashtags, key=hashtags.get, reverse=True)
# sorted_list = sorted_list[:250]

# print "Total tweets extracted: " , total_count
# print "Total unique tweets: " , ctr

# for w in sorted_list:
#     # per = float(hashtags[w]) / ctr * 100
#     # print hashtags[w], '\t', per, '\t', w
#     print w


"""
/home/prabhakar/Documents/btp/train-data/dataset/AlQaeda
/home/prabhakar/Documents/btp/train-data/dataset/Daesh
/home/prabhakar/Documents/btp/train-data/dataset/GameOfThrones
/home/prabhakar/Documents/btp/train-data/dataset/IPL
/home/prabhakar/Documents/btp/train-data/dataset/ISIL
/home/prabhakar/Documents/btp/train-data/dataset/ISIS
/home/prabhakar/Documents/btp/train-data/dataset/IslamicState
/home/prabhakar/Documents/btp/train-data/dataset/Taliban
/home/prabhakar/Documents/btp/train-data/dataset/Wahhabism
"""