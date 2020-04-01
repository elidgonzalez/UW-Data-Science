import sys
import json
import string
    
def freq(hashtags, totals):
    for hashtag in hashtags:
        if hashtag['text'] in totals:
            totals[hashtag['text']] += 1.0
        else:
            totals[hashtag['text']] = 1.0
    

def main():
    tweet_file = open(sys.argv[1])
    tweets = []
    for line in tweet_file:
        tweets.append(json.loads(line))
    totals = {}
    for tweet in tweets:
        if len(tweet['entities']['hashtags']) > 0:
            freq(tweet['entities']['hashtags'], totals)
    sorted_totals = sorted(totals.items(), key=lambda total: total[1], reverse=True) 
    for i in range(10):
        print sorted_totals[i][0], sorted_totals[i][1]

if __name__ == '__main__':
    main()
