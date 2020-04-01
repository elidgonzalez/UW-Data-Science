import sys
import json
import string


def main():
	tweet_file = open(sys.argv[1])
	tweets = []
	filtered = []
	for line in tweet_file:
		tweets.append(json.loads(line))
	for tweet in tweets:
		if 'coordinates' in tweet:
			if tweet['coordinates']:
				filtered.append(tweet)
	print len(filtered)
   	with open('samples.json', 'w') as samples:
   		for tweet in filtered:
   			json.dump(tweet, samples)
   			samples.write('\n')

if __name__ == '__main__':
	main()