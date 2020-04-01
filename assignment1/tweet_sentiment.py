import sys
import json
import string
    
def score_tweet(tweet, scores):
    words =  tweet.split(' ')
    score = 0
    for word in words:
        filtered_word = like(word, scores.keys())
        if filtered_word:
            score += scores[filtered_word]
    return score
 
def like(main, sublst):
    for sub in sublst:
        #print main, sub
        if sub.decode('utf8') in main:
            return sub
    return None
            

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    tweets = []
    for line in tweet_file:
        tweets.append(json.loads(line))
    scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    final_tally = []
    for tweet in tweets:
        final_tally.append(score_tweet(tweet['text'], scores))
    for tally in final_tally:
        print tally

if __name__ == '__main__':
    main()

