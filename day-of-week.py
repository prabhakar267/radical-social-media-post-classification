import os
import json
from datetime import datetime

total_count = 0
ctr = 0
tweets_day = [0]*7

# Add Dataset Path
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
		day = int(tweet_datetime.strftime("%w"))
		tweets_day[day] += 1

print tweets_day