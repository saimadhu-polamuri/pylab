#!/usr/bin/env python
#File name: text_read.py
#Author : saimadhu
#Date: 20-Oct-2014
#About: Converting normal text specific date
import re
#from sample_dateparser import *
dates = []
regex1 = re.compile(r'''(?:(mon|tue|wed|thu|fri|sat|sun|mo|tu|we|th|fr|sa|su|m|w|f|thurs)\s*)?  #weekday
    ( (?:\d{1,2}(?:[:]\d{1,2})?)\s*(?:[ap][.]?m.?)  \s*[-|to]+\s*   (?:\d{1,2}(?:[:]\d{1,2})?)\s*(?:[ap][.]?m[.]?) # hour:min period
    )''',re.VERBOSE | re.IGNORECASE)
regex2 = re.compile(r'''((?:January|March|May|may|July|August|October|December|September|April|June|November|February|Jan|jan|Mar|mar|july|august|Aug|aug|october|Oct|oct|december|Dec|dec|september|Sep|sep|april|Apr|apr|june|Jun|jun|november|Nov|nov|february|Feb|feb)\s(?:[0-9][0-9]*))''')
regex3 = re.compile(r'''(?:(mon|tue|wed|thu|fri|sat|sun|mo|tu|we|th|fr|sa|su|m|w|f|thurs)\s*)  #weekday
    ( (?:\d{1,2}(?:[:]\d{1,2})?)\s*(?:[ap][.]?m.?)  \s*[-|to]+\s*   (?:\d{1,2}(?:[:]\d{1,2})?)\s*(?:[ap][.]?m[.]?) # hour:min period
    )''',re.VERBOSE | re.IGNORECASE)
regex4 = re.compile(r'''\d\d/\d\d''')
regex5 = re.compile(r'''(?:Daily:|Daily|daily)\s(?:[A-Z][a-z][a-z]-[A-Z][a-z][a-z] [\d\d.\d\d]+[a|p]m-[\d\d.\d\d]+[a|p]m)''')
regex6 = re.compile(r'''(Mon|Tue|wed|Thu|Fri|Sat|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)''')
regex7 = re.compile(r'''((?:Mon|Tue|Wed|Thu|Fri|Sat)\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s[\d\d]+)''')
regex8 = re.compile(r'''((?:Mon|Tue|Wed|Thu|Fri|Sat)-(?:Mon|Tue|Wed|Thu|Fri|Sat)\s[\d\d.\d\d]+[a|p]m-[\d\d.\d\d]+[a|p]m)''')
regex9 = re.compile(r'''(Mondays|Tuesdays|Wednesdays|Thursdays|Fridays|Saturdays|Sundays)''')
regex10 = re.compile(r'''((?:Mon|Tue|wed|Thu|Fri|Sat|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)-(?:Mon|Tue|wed|Thu|Fri|Sat|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday))''')
regex11 = re.compile(r'''((?:[\d]+|[\d]+.[\d]+)[a|p]m\sto\s(?:[\d]+|[\d]+.[\d]+)[a|p]m)''')
regex12 = re.compile(r'''((?:[\d]|[\d][\d]|[\d].[\d]+|[\d][\d].[\d]+)(?:[a|p]m))''')
regex13 = re.compile(r'''(?:Daily:|Daily|daily)\s+[\d]+-[\d]+\s*(?:[a|p]m)''' )
regexList = [regex5,regex2,regex3,regex4,regex7,regex8,regex9,regex10,regex11,regex6,regex13,regex12]
with open('Date Formats - Sheet1.csv', 'rb') as csvfile:
    for row in csvfile:
    	gotMatch = False
    	for regex in regexList:
    		s = re.findall(regex,row)
    		if s:
    			gotMatch = True
    			break
    	if gotMatch:
    		dates.append(s)
for element in dates:
	print element
print "lenght: ",len(dates)