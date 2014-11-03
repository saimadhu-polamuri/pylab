#!/usr/bin/env python
# urltopdf.py
#Author : saimadhu
#Date: 07-Oct-2014
#About: Converting url to pdf format and download

# sudo apt-get install wkhtmltopdf
# sudo pip install pdfkit

# Required Packages
import pdfkit
#Function to convert website to pdf
def url_pdf(url,pdf_name):

	pdfkit.from_url(url, pdf_name+'.pdf')
	print "web page successfully converted to pdf............."
#Main Function
def main_function():
	url = 'dataaspirant.wordpress.com'
	name ="dataaspirant"
	url_pdf(url,name)
#calling main Function	
main_function()	