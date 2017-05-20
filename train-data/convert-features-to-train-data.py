import os
import json


dataset_path = "feature-vectors"

X_pro = []
Y_pro = []
X_con = []
Y_con = []
X = []
Y = []

dataset_chosen = "con-radical"
final_dataset_path = dataset_path + "/" + dataset_chosen

ctr = 0
for dp, dn, filenames in os.walk(final_dataset_path):
	count = len(filenames)
	for f in filenames:
		ctr += 1
		filepath = final_dataset_path + "/" + f
		with open(filepath) as x:
			data = json.load(x)
			X_con.append(data)
		print f, ctr, count
	Y_con = [0] * count


dataset_chosen = "pro-radical"
final_dataset_path = dataset_path + "/" + dataset_chosen

ctr = 0
for dp, dn, filenames in os.walk(final_dataset_path):
	count = len(filenames)
	for f in filenames:
		ctr += 1
		filepath = final_dataset_path + "/" + f
		with open(filepath) as x:
			data = json.load(x)
			X_pro.append(data)
		print f, ctr, count
	Y_pro = [1] * count


X = X_pro + X_con
Y = Y_pro + Y_con

with open("final_results_X", 'w') as f:
	json.dump(X, f)

with open("final_results_Y", 'w') as f:
	json.dump(Y, f)
