import os
import json


dataset_path = "feature-vectors"

Z = []

dataset_chosen = "test-data"
final_dataset_path = dataset_path + "/" + dataset_chosen

ctr = 0
for dp, dn, filenames in os.walk(final_dataset_path):
	count = len(filenames)
	for f in filenames:
		ctr += 1
		filepath = final_dataset_path + "/" + f
		with open(filepath) as x:
			data = json.load(x)
			Z.append(data)
		print f, ctr, count


with open("test-data", 'w') as f:
	json.dump(Z, f)
