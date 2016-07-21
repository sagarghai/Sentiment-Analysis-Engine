"""
FILE : main.py
DESCRIPTION : This code is the utility by which user need not to
	know any deatils of the framework rather use this abstraction.

Run Command: main.py [json file name]

AUTHOR : Tushar Gupta

BUG FIXES :
		June 22,2016
"""
import sys
import sentimental
import nltk
import Hashtag
import twitter
import preprocess
from nltk.corpus import stopwords

try:
    count = sys.argv[2]
except:
    count = 10
filename = sys.argv[1]
k = (str)(raw_input('Enter your preference here > '))
twitter.takename(k, filename, count)
import parser
listoftweets = parser.parser(filename)

# Hashtag.hashtag(listoftweets)

splitter = sentimental.Splitter()
postagger = sentimental.POSTagger()
dicttagger = sentimental.DictionaryTagger(['positive-words.yml', 'negative-words.yml'])
filename = (str)(raw_input('Enter the filename to store individual tweet score > '))
if 'csv' not in filename.split('.'):
    filename = filename + '.csv'
file2 = open(filename, 'w+')
filename1 = (str)(raw_input('Enter the filename to store keywords > '))
file1 = open(filename1, 'w+')
sum = 0
for tweet in listoftweets:
    tkt = []
    stop = stopwords.words('english')
    tweet_tokens = preprocess.preprocess(tweet)
    for i in tweet_tokens:
        if i not in stop and len(i) >= 4:
            tkt.append(i)
    tkts = ', '.join(tkt)
    tkts = tkts + '\n'
    file1.write(tkts)
    splitted_sentences = splitter.split(tweet)
    pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
    dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
    a = sentimental.sentiment_score(dict_tagged_sentences)
    keywords = sentimental.keyword_token(dict_tagged_sentences)
    keys = ','.join(keywords)
    sum = sum + a
    tweet = tweet.replace(',', "")
    output = tweet + ',' + keys + ',' + (str)(a) + '\n'
    file2.write(output)
print 'Total sentiment score is :', sum
