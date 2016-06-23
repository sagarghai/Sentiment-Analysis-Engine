""" 
FILE : parser.py
DESCRIPTION : Code to find out all the Hashtags in a particular tweet.

AUTHOR : Tushar Gupta

BUG FIXES :
		June 22,2016  
"""
import sys
import csv
import re

#import parser

def hashtag(tweets):
	listofhashtag = []
	tag = ""
	flag = False
	for tweet in tweets:
		lengthoftweet = 0
		for letter in tweet:
			if(letter == '#'):
				flag = True
			if(flag == True):
				tag += letter
				if (not re.match('^[\w\d_()#]*$', letter)) or lengthoftweet == len(tweet) - 1:
					flag = False
					listofhashtag.append(tag[1:])
					tag = ""
			lengthoftweet += 1

	print listofhashtag

#hashtag(["IPL 2916: Playing alongside Virat Kohli is a 'huge buzz' for me, says Shane Watson https://t.co/O1mXPDp3Gj #Cricket"])
