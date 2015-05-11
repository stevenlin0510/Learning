#!/usr/bin/env python

import re
import sys

PY_VERSION = sys.version_info[0]
if PY_VERSION == 2:
	import urllib2
if PY_VERSION == 3:
	import urllib


def getHTML(urls):
	htmlfile = urllib2.urlopen(urls)
	htmltext = htmlfile.read()
	return htmltext

def getImage(source):
	RE = r'src="(.*.jpg)"'
	imgre = re.compile(RE)
	images = re.findall(imgre, source)
	for i in images:
		print i
	

url = "http://jandan.net/ooxx/page-"
for page_number in range(1390,1398):
	geturl = url + str(page_number)
	print geturl
	source = getHTML(geturl)
	print getImage(source)
# print getHTML(url)