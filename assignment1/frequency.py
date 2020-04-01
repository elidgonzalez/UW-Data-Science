import sys
import json
    
def freq(tweets):
    frequency = {}
    total = 0
    for tweet in tweets:
        if 'text' in tweet:
            words =  tweet['text'].encode('utf-8').split()
            for word in words:
                total += 1
                if word in frequency:
                    frequency[word] += 1
                else:
                    frequency[word] = 1
    return total, frequency
    

def main():
    tweet_file = open(sys.argv[1])
    tweets = []
    for line in tweet_file:
        tweets.append(json.loads(line))
    total, frequency = freq(tweets)
    for word in sorted(frequency, key=frequency.get, reverse=True):
        print word, '%.4f' %(float(frequency[word])/total)

if __name__ == '__main__':
    main()
