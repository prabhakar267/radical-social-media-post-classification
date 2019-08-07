import os
import json
from datetime import datetime

total_count = 0
ctr = 0
tweets_time = [0]*24

# Add dataset path
selected_dataset = None

for dp, dn, filenames in os.walk(selected_dataset):
	total_count += len(filenames)
	for f in filenames:
		ctr += 1
		if ctr % 100 == 0:
			print ctr
		
		
		file_path = os.path.join(dp, f)
		with open(file_path) as data_file:
			data = json.load(data_file)

		tweet_datetime = datetime.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
		hour = int(tweet_datetime.strftime("%H")) - 1
		tweets_time[hour] += 1

print tweets_time