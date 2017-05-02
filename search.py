import json
import urlparse

from TwitterAPI import TwitterAPI

with open('hashtags') as f:
	hashtags_list = f.readlines()
hashtags_list = map(str.strip, hashtags_list)

for HASHTAG in hashtags_list:
	# HASHTAG = raw_input("Enter hashtag:")
	SEARCH_TERM = '#' + HASHTAG

	CONSUMER_KEY = 'pxWu3KD8bthx0ERuzA8azh61e'
	CONSUMER_SECRET = 'viOitYFe4s29Lj6ibM3ABsnwT6dAdYWPriLUCujsljfXNUEKx1'
	ACCESS_TOKEN_KEY = '1954715881-X89rhEPJLBdmDFCfHK9Gnb1uwDTVl3YZszK8abD'
	ACCESS_TOKEN_SECRET = 'KMCmjw37Th6V0W2xs87NoohSEbspzezShyr2pkdwSewRz'

	dir_name = "Real"
	tweet_dir = dir_name + "/" + HASHTAG
	exit_flag = False

	api = TwitterAPI(CONSUMER_KEY,
	                 CONSUMER_SECRET,
	                 ACCESS_TOKEN_KEY,
	                 ACCESS_TOKEN_SECRET)


	r = api.request('search/tweets', {
		'q': SEARCH_TERM,
		'include_entities': 1,
		"count": 100
	})

	while r.status_code == 200:
		json_response = r.json()
		
		if 'next_results' not in json_response['search_metadata']:
			exit_flag = True
		else:
			next_results_url = json_response['search_metadata']['next_results']
			next_results_params = dict(urlparse.parse_qsl(urlparse.urlsplit(next_results_url).query))
			min_id = next_results_params['max_id']

		json_response = json_response['statuses']

		for tweet in json_response:
			filepath = tweet_dir + '/' + tweet['id_str']
			with open(filepath, 'w+') as outfile:
				json.dump(tweet, outfile)
				print tweet['id_str']


		if exit_flag:
			break

		r = api.request('search/tweets', {
			'q': SEARCH_TERM,
			'include_entities': 1,
			"count": 100,
			"max_id": min_id,
		})

	print r.text