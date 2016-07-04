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
#from sentimental import DictionaryTagger
import parser
import nltk
import Hashtag
import twitter

twitter.takename("") 
filename = sys.argv[1]
listoftweets = parser.parser(filename)
#print li 

Hashtag.hashtag(listoftweets)



