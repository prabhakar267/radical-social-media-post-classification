import json

filename = "tweet_features_all_nouns.json"

with open(filename) as f:
	data = json.load(f)

sorted_list = sorted(data, key=data.get, reverse=True)
sorted_list = sorted_list[:500]

sorted_list = [x.lower() for x in sorted_list]

sorted_list.remove("amp")
sorted_list.remove("com")
sorted_list.remove("par")
sorted_list.remove("the")
sorted_list.remove("cia")
sorted_list.remove("did")
sorted_list.remove("tel")
sorted_list.remove("don")

# print len(sorted_list)

sorted_list = list(set(sorted_list))
sorted_list = [x.encode('ascii', 'ignore') for x in sorted_list]

print sorted_list
print len(sorted_list)
