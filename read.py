import json
import pickle

filename = "dump/test"
prev_results = pickle.load(open(filename, "rb"))

# x = max(prev_results, key=lambda ev: ev['id'])
# # print json.dumps(x, indent=4, sort_keys=True)
# # print x
# # exit()

# print x['id']
# print "\n"

for i in prev_results:
	# print i
	print json.dumps(i, indent=4, sort_keys=True)
	# print i['id']
	# print i
	exit()