#!/usr/bin/env python
#File name: dateparser.py
#Author : saimadhu
#Date: 20-Oct-2014
#About: Converting normal text date format

# Required Packages

from dateutil import parser
from dateutil import rrule
from datetime import timedelta,datetime
import parsedatetime,time
import re
import parsedatetime as pdt
import time 
from dateutil.relativedelta import *
import pandas as pd
from datetime import date, timedelta as td
#from datetime import *
from dateutil.relativedelta import *
import calendar

#For getting date and time
def get_datetime(date):
	result = parser.parse(date,dayfirst=True)
	return result

#for finding number of dates
def dates_remain(start_date,end_date):
	first_date = get_datetime(start_date)
	last_date = get_datetime(end_date)
	result = relativedelta(last_date,first_date)
	return first_date,last_date,result

# For return length of the dic or list
def lengthof(data):
	return len(data)

#For generating dates between start date and end date
def start_end_dates(start_date,end_date):
	dates_list = []
	list_date = []
	d1 = get_datetime(start_date)
	d2 = get_datetime(end_date)
	delta = d2-d1
	for i in range(delta.days + 1):
		temp = d1 + td(days=i)
		dates_list.append(temp)
	return dates_list

#Function to generate dates for regex3 regular expression	
def regex3_date(line):
	date = []
	weekday = line[0]
	time = line[1].split('-')
	start_day = get_datetime(weekday+time[0])
	end_day = get_datetime(weekday+time[1])
	date.append(start_day)
	date.append(end_day)
	return  date

#Generating weekdays :
def week_days_generate(weekday):
	dates = []
	short_week = weekday[0:3]
	start_date = get_datetime(short_week)
	dates.append(start_date)
	how_weeks = 5
	for i in range (1,how_weeks):
		nextweek = start_date+relativedelta(weeks=+i)
		dates.append(nextweek)
	return dates	

#Converting string to start date and end date	
def time_to_time(string):
	dates = []
	sample = string.split()
	start_date = get_datetime(sample[0])
	end_date = get_datetime(sample[2])
	dates.append(start_date)
	dates.append(end_date)
	return dates

#finding weekday value
def weekday_value(weekday):
	weekdays_list = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
	weekdays_dic = {'Sun':1,'Mon':2,'Tue':3,'Wed':4,'Thu':5,'Fri':6,'Sat':7}
	day_value = 0
	for element in weekdays_list:
		if weekday == element:
			day_value = weekdays_dic[element]
			break
	return day_value	

#Finding difference between 2 week days
def weekdays_diff(start_weekday,last_weekday):
	start_value = 0
	end_value = 0
	weekday_difference = 0
	start_value = weekday_value(start_weekday)
	end_value = weekday_value(last_weekday)
	if start_value < end_value:
		weekday_difference = end_value - start_value
	if start_value > end_value:
		end_value = end_value + 7
		weekday_difference = end_value - start_value
	return weekday_difference	

#Generating days between 2 weekdays
def weekdays_generation(start_date,difference):
	dates_list = []
	last_date = start_date + timedelta(difference)
	delta = last_date-start_date
	for i in range(delta.days + 1):
		temp = start_date + td(days=i)
		dates_list.append(temp)
	return dates_list	

#For generating list of dates
def long_dates(data):
	temp_list = []
	for element in data:
		temp_list.append(get_datetime(element))
	return temp_list

#Generating dates between to dates in pandas				
def start_end_date_generation(start_date,end_date):
	dates = []
	first_date = get_datetime(start_date)
	last_date = get_datetime(end_date)
	dates_left = last_date - first_date
	datelist = pd.date_range(first_date, last_date).tolist()
	return datelist

#Function to generate dates for regex6 regular expression	
def regex6_date_generation(list_list):
	dates = []
	for element in list_list:
		dates.append(get_datetime(element))
	return dates	

#Function to generate dates for regex13 regular expression
def regex13_date_generation(start_date,end_date):
	dates = []
	first_date = get_datetime(start_date)
	last_date = get_datetime(end_date)
	dates.append(first_date)
	dates.append(last_date)
	for i in range(1,30):
		beginning = first_date + td(days=i)
		ending = last_date + td(days=i)
		dates.append(beginning)
		dates.append(ending)
	return dates	

# Finding date formats from text
def date_data(file_name):
	dates = []
	regex1 = re.compile(r'''(?:(mon|tue|wed|thu|fri|sat|sun|mo|tu|we|th|fr|sa|su|m|w|f|thurs)\s*)?  #weekday
    	( (?:\d{1,2}(?:[:]\d{1,2})?)\s*(?:[ap][.]?m.?)  \s*[-|to]+\s*   (?:\d{1,2}(?:[:]\d{1,2})?)\s*(?:[ap][.]?m[.]?) # hour:min period
    	)''',re.VERBOSE | re.IGNORECASE)

	regex2 = re.compile(r'''((?:January|March|May|may|July|August|October|December|September|April|June|November|February|Jan|jan|Mar|mar|july|august|Aug|aug|october|Oct|oct|december|Dec|dec|september|Sep|sep|april|Apr|apr|june|Jun|jun|november|Nov|nov|february|Feb|feb)\s(?:[0-9][0-9]*))''')
	regex3 = re.compile(r'''(?:(mon|tue|wed|thu|fri|sat|sun|mo|tu|we|th|fr|sa|su|m|w|f|thurs)\s*)  #weekday
	    ( (?:\d{1,2}(?:[:]\d{1,2})?)\s*(?:[ap][.]?m.?)  \s*[-|to]+\s*   (?:\d{1,2}(?:[:]\d{1,2})?)\s*(?:[ap][.]?m[.]?) # hour:min period
	    )''',re.VERBOSE | re.IGNORECASE)
	regex4 = re.compile(r'''\d\d/\d\d''')
	regex5 = re.compile(r'''(?:Daily:)\s(?:[A-Z][a-z][a-z]-[A-Z][a-z][a-z] [\d\d.\d\d]+[a|p]m-[\d\d.\d\d]+[a|p]m)''')
	regex6 = re.compile(r'''(Mon|Tue|wed|Thu|Fri|Sat|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)''')
	regex7 = re.compile(r'''((?:Mon|Tue|Wed|Thu|Fri|Sat)\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s[\d\d]+)''')
	regex8 = re.compile(r'''((?:Mon|Tue|Wed|Thu|Fri|Sat)-(?:Mon|Tue|Wed|Thu|Fri|Sat)\s[\d\d.\d\d]+[a|p]m-[\d\d.\d\d]+[a|p]m)''')
	regex9 = re.compile(r'''(Mondays|Tuesdays|Wednesdays|Thursdays|Fridays|Saturdays|Sundays)''')
	regex10 = re.compile(r'''((?:Mon|Tue|wed|Thu|Fri|Sat|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)-(?:Mon|Tue|wed|Thu|Fri|Sat|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday))''')
	regex11 = re.compile(r'''((?:[\d]+|[\d]+.[\d]+)[a|p]m\sto\s(?:[\d]+|[\d]+.[\d]+)[a|p]m)''')
	regex12 = re.compile(r'''((?:[\d]|[\d][\d]|[\d].[\d]+|[\d][\d].[\d]+)(?:[a|p]m))''')
	regex13 = re.compile(r'''(?:Daily:|Daily|daily)\s+[\d]+-[\d]+\s*(?:[a|p]m)''' )
	regexList = [regex5,regex2,regex3,regex4,regex7,regex8,regex9,regex10,regex11,regex6,regex13,regex12]
	with open(file_name, 'rb') as csvfile:
	    for row in csvfile:

			gotMatch = False
	    		for regex in regexList:
	    			temp = []
		    		s = re.findall(regex,row)
		    		if s:
		    			gotMatch = True
		    			break
		    	if gotMatch and (regex == regex4 or regex == regex2):
		                 if len(s) == 1:
		                    temp = get_datetime(s[0])
		                 if len(s) == 2:
		                	temp = start_end_dates(s[0],s[1])
		            	 dates.append(temp)    	
		        if gotMatch and (regex == regex8):
		        	if len(s) == 1:
		        		sample = s[0].split()
		        		weekdays = sample[0].split('-')
		        		time = sample[1].split('-')
		        		start_date = weekdays[0]
		        		end_date = weekdays[1]
		        		start_time = float(re.findall('[\d]+.[\d]+|[\d]+',time[0])[0])
		        		end_time = float(re.findall('[\d]+.[\d]+|[\d]+',time[1])[0]) + 12
		        		dif_time = end_time -start_time
		        		weekday_diff_value = weekdays_diff(start_date,end_date)
		        		input_start_date = get_datetime(start_date+time[0])
		        		temp = weekdays_generation(input_start_date,weekday_diff_value)
		        		last_date = temp[-1] + timedelta(hours=dif_time)
		        		temp.append(last_date)
		    			dates.append(temp)
		    	
		    	if gotMatch and (regex == regex5):
		    		if len(s) == 1:
		    			#print s
		    			sample = s[0].split()
		    			weekdays = sample[1].split('-')
		    			time = sample[2].split('-')
		    			#print time[0],time[1]
		    			start_time = float(re.findall('[\d]+.[\d]+|[\d]+',time[0])[0])
		        		end_time = float(re.findall('[\d]+.[\d]+|[\d]+',time[1])[0]) + 12
		        		dif_time = end_time -start_time
		        		#print start_time,end_time
		    			week_start_day = weekdays[0]
		    			week_end_day = weekdays[1]
		    			weekday_diff_value = weekdays_diff(week_start_day,week_end_day)
		    			input_start_date = get_datetime(week_start_day+time[0])
		    			temp = weekdays_generation(input_start_date,weekday_diff_value)
		    			last_date = temp[-1] + timedelta(hours=dif_time)
		    			temp.append(last_date)
		    			print temp
		    	if gotMatch and (regex == regex3):
		    		if len(s) == 1:
		    			temp = regex3_date(s[0])
		    			dates.append(temp)
		    	if gotMatch and (regex == regex9):
		    		temp = week_days_generate(s[0])
		    		dates.append(temp)
		    	if gotMatch and (regex == regex11):
		    		temp = time_to_time(s[0])
		    		dates.append(temp)
		    	if gotMatch and (regex == regex6):
		    		temp = regex6_date_generation(s)
		    		#print temp
		    		dates.append(temp)
		    	if gotMatch and (regex == regex7):
		    		if len(s) == 1:
		    			temp = get_datetime(s[0])
		    			dates.append(temp)
		    		if len(s) == 2:
		    			start_date = s[0]
		    			end_date = s[1]	
		    			temp = start_end_dates(start_date,end_date)
		    			dates.append(temp)
		    	if gotMatch and (regex == regex12):
		    		if len(s) == 1:
		    			temp = get_datetime(s[0])
		    			dates.append(temp)
		    		if len(s) > 1:
		    			temp = regex6_date_generation(s)
		    			dates.append(temp)
		    	if gotMatch and (regex == regex13):
		    		sample = s[0].split()
		    		times =  sample[1].split('-')
		    		start_date = times[0]+'am'
		    		end_date = times[1]
		    		temp = regex13_date_generation(start_date,end_date)
		    		dates.append(temp)
		    		#print temp		

	return dates

# Main Function
def main_function():
	file_name = 'Date Formats - Sheet1.csv'
	dates_list = date_data(file_name)
	for element in dates_list:
		print element
	print "lenght: ",len(dates_list)	
	#sample = data_specific_format(dates_list)
main_function()		