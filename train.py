import json
import os
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

base_directory = "sample-data"
results_dir = "results"

train_X_path = os.path.join(base_directory, "final_results_X")
train_y_path = os.path.join(base_directory, "final_results_Y")
test_X_path = os.path.join(base_directory, "test-data")


with open(train_X_path, "r") as fx:
	X = json.load(fx)

with open(train_y_path, "r") as fy:
	Y = json.load(fy)

with open(test_X_path, "r") as fz:
	Z = json.load(fz)
total_size_of_training_data = len(Z)

print "Test and training data loaded" 
print "#" * 100


clfs = {
	'svm': svm.SVC(kernel="rbf", gamma=1000),
	'random-forest': RandomForestClassifier(max_depth=5, max_features=1, n_estimators=10),
	'adaboost': AdaBoostClassifier()
}
for clf_name, clf in clfs.items():
	print "Fitting {}".format(clf_name)
	clf.fit(X,Y)
	print "Training complete"

	prediction_results = clf.predict(Z)
	clean_prediction_results = []
	error = 0
	for i in prediction_results:
		clean_prediction_results.append(int(i))
		if i == 1:
			error += 1

	print "Predictions complete"
	print total_size_of_training_data, "\t", error
	print "#" * 100
	
	filepath = os.path.join(results_dir, clf_name)
	with open(filepath, 'w') as f:
		json.dump(clean_prediction_results, f)
