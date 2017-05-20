import json
from sklearn import svm
#from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier


with open("final_results_X", "r") as fx:
	X = json.load(fx)

with open("final_results_Y", "r") as fy:
	Y = json.load(fy)

with open("test-data", "r") as fz:
	Z = json.load(fz)
total_size_of_training_data = len(Z)

print "Test and training data loaded" 

clf = svm.SVC(kernel="rbf", gamma=1000)
#clf = RandomForestClassifier(max_depth=5, max_features=1, n_estimators=10)
#clf = AdaBoostClassifier()
clf.fit(X,Y)

print "Training complete"

prediction_results = clf.predict(Z)

clean_prediction_results = []
error = 0
for i in prediction_results:
	clean_prediction_results.append(i)
	if i == 1:
		error += 1

print "Predictions complete"

results_dir = "results"
method = "svm"
filepath = results_dir + "/" + method
with open(filepath, 'w') as f:
	json.dump(clean_prediction_results, f)

print total_size_of_training_data, "\t", error

#clf = svm.SVC()
#clf.fit(X, y)  
#print clf

