import json
import urlparse

from TwitterAPI import TwitterAPI

HASHTAG = "ISIL"
SEARCH_TERM = '#' + HASHTAG

CONSUMER_KEY = 'dACHUkdxoeoGhj33VbhJbhu5I'
CONSUMER_SECRET = 'Oyhi6fkORU7NEM3KGFa0vEAVX2FVKijYFsAogxsO96ZTQObx9G'
ACCESS_TOKEN_KEY = '865560603292614658-zK5KgbeItsuwrmCccmA3cjsb5s4uwDE'
ACCESS_TOKEN_SECRET = 'fbvd9NDzsMdAiTeUmqLCa9QpL4L3suiyuRW0O7qXNvk7F'

dir_name = "dataset"
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
