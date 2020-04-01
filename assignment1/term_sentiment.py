import sys
import json
import string

def score_tweet(tweet, scores):
    words =  tweet.split(' ')
    score = 0
    null_words = []
    for word in words:
        filtered_word = like(word, scores.keys())
        if filtered_word:
            score += scores[filtered_word]
        else:
            null_words.append(word)
    return null_words, score

def like(main, sublst):
    for sub in sublst:
        if sub in main.encode('utf-8'):
            return sub
    return None

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    tweets = []
    for line in tweet_file:
        tweets.append(json.loads(line))
    scores = {}
    weighted_scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = float(score)
    for tweet in tweets:
        null_words, score = score_tweet(tweet['text'], scores)
        for word in null_words:
            if word in weighted_scores:
                weighted_scores[word].append(score)
            else:
                weighted_scores[word] = [score]
    for k,v in weighted_scores.items():
        print k.encode('utf-8'), sum(v)/len(v)
    

if __name__ == '__main__':
    main()
