import csv
import sys

file1 = open("dictionary/negative-words.txt",'r')
file2 = open("negative-words.yml",'w')

for line in file1:
	string = line[0:len(line) - 1] + ": " + "[negative]" + '\n'
	print string 
	file2.write(string)

file2.close()