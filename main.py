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
import parser
import nltk
import Hashtag
# import twitter

# twitter.takename("") 
filename = sys.argv[1]
listoftweets = parser.parser(filename)
#print li 

Hashtag.hashtag(listoftweets)

splitter = sentimental.Splitter()
postagger = sentimental.POSTagger()
# dicttagger = sentimental.DictionaryTagger([ 'positive-words.yml', 'negative-words.yml'])

for tweet in listoftweets:
	splitted_sentences = splitter.split(tweet)
	# print (splitted_sentences)
	pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
	print(pos_tagged_sentences)

# 	dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
# 	sentiment_score(dict_tagged_sentences)

