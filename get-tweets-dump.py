import os
import json
import urlparse

import utils as u
from constants import DATA_DIR, TWEETS_DUMP_DIR, TWEET_COUNT


twitter_client = u.get_twitter_client()
search_hashtags = u.load_search_hashtags()
is_last_result = False

for hashtag in search_hashtags:
    search_query = "#{}".format(hashtag)
    tweet_output_path = os.path.join(DATA_DIR, TWEETS_DUMP_DIR, search_query)
    
    resp = twitter_client.request('search/tweets', {
        'q': search_query,
        'include_entities': 1,
        "count": TWEET_COUNT
    })

    while resp.status_code == 200:
        tweet_json_response = resp.json()
        
        if 'next_results' not in json_response['search_metadata']:
            is_last_result = True
        else:
            next_results_url = json_response['search_metadata']['next_results']
            next_results_params = dict(urlparse.parse_qsl(urlparse.urlsplit(next_results_url).query))
            request_maximum_id = next_results_params['max_id']

        tweets = tweet_json_response['statuses']

        for tweet in tweets:
            tweet_id = tweet['id_str']
            tweet_filepath = os.path.join(tweet_output_path, tweet_id)
            
            try:
                u.write_tweet(tweet_filepath, tweet)
            except IOError as e:
                print e
        
        if is_last_result:
            break

        resp = twitter_client.request('search/tweets', {
            'q': search_query,
            'include_entities': 1,
            "count": TWEET_COUNT,
            "max_id": request_maximum_id,
        })
