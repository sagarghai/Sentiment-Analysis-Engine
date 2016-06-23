""" 
FILE : parser.py
DESCRIPTION : This code is basically made to parse the data which 
          we have got from the tweeter API. Basically we are extracting 
          the tweet that a user has made, ignoring all other data.

AUTHOR : Tushar Gupta

BUG FIXES :
		April 11,2016  
"""

import sys
import csv
import math
import nltk
import re

def parser(filename):
	fp = open(filename, "r")
	# temp list to store all the tweet
	tweet = [] 
	for line in fp:
		l = re.findall(r'text=u(.*?), is_quote_status',line)
		tweet.append(l[0])
		#print l[0]
	return tweet

# Get file name by command line argument




