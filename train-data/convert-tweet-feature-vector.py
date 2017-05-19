import os
import json
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
import enchant
from datetime import datetime

from constants import HASHTAGS, WORDS, PROPER_NOUN_POS_TAGS
from utils import remove_hashtags


enchant_dictionary = enchant.Dict("en_US")
lmtzr = WordNetLemmatizer()


length_of_hashtags = len(HASHTAGS)
length_of_words = len(WORDS)
length_of_time_features = 24 + 7

total_length = length_of_hashtags + length_of_words + length_of_time_features

words_added = 0
total_count = 0
ctr = 0
dataset_path = "dataset"
feature_vector_path = "feature-vectors"

selected_dataset = "IslamicState"

final_dataset_path = dataset_path + "/" + selected_dataset
final_feature_vector_path = feature_vector_path + "/" + selected_dataset

for dp, dn, filenames in os.walk(final_dataset_path):
	total_count += len(filenames)

	for f in filenames:
		ctr += 1
		file_path = os.path.join(dp, f)
		save_file_path = os.path.join(final_feature_vector_path, f)


		if os.path.isfile(save_file_path):
			continue

		hashtags_feature_vector = [0] * length_of_hashtags
		words_feature_vector = [0] * length_of_words
		time_feature_vector = [0] * length_of_time_features

		with open(file_path) as data_file:
			data = json.load(data_file)	


		# hashtags feature-vectors
		for hashtag in data['entities']['hashtags']:
			clean_hashtag_string = hashtag['text'].lower()
			if clean_hashtag_string in HASHTAGS:
				hashtag_index = HASHTAGS.index(clean_hashtag_string)
				hashtags_feature_vector[hashtag_index] = 1


		# words feature-vectors
		clean_tweet_text = remove_hashtags(data['text'])
		tokens = nltk.word_tokenize(clean_tweet_text)
		pos_tag_data = nltk.pos_tag(tokens)

		for token_tuple in pos_tag_data:
			noun_word = token_tuple[0]
			clean_noun_word = noun_word

			if clean_noun_word:
				if token_tuple[1] in PROPER_NOUN_POS_TAGS and enchant_dictionary.check(clean_noun_word):
					lemmatized_word = lmtzr.lemmatize(clean_noun_word)
					
					if lemmatized_word in WORDS:
						word_index = WORDS.index(lemmatized_word)
						words_feature_vector[word_index] = 1
						words_added += 1


		# time feature-vectors
		tweet_datetime = datetime.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
		hour = int(tweet_datetime.strftime("%H")) - 1
		day = int(tweet_datetime.strftime("%w"))
		time_feature_vector[hour] = 1
		time_feature_vector[day + 24] = 1


		final_feature_vector = hashtags_feature_vector + words_feature_vector + time_feature_vector

		with open(save_file_path, 'w') as save_file:
			json.dump(final_feature_vector, save_file)
			print f, '\t', ctr, '\t', total_count - ctr, '\t', words_added