#!/usr/bin/env python
# url_domine.py
#Author : saimadhu
#Date: 25-sept-2014
#About: Converting Decoded url to domine name

# Required Packages
import urllib
from urlparse import urlparse

# Generating domine name from decoded url
def decodedurl_dominename(url):
	decoded_url = urllib.unquote(url).decode('utf8') 
	final_url = decoded_url.replace("&_", "")
	url_slice = urlparse(final_url)
	return url_slice.netloc.replace("www.","").replace(".com","")

# calling function
url = 'http%3A%2F%2Fwww.theperfumeshop.com%2Ffcp%2Fproduct%2Ffragrances%2FDesigner-Perfumes%2FAlien%2F1581&_'
domine_name = decodedurl_dominename(url)
print domine_name
