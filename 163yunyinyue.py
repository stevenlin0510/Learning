#!/usr/bin/env python

import urllib2
import re

def getHTML(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	html_file = response.read()
	return html_file

def getVideo(html):
	reg = r'hurl=(.+?\.jpg)'
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	return imglist

# for num in range(393004, 393007):
# 	print num
# 	html = getHTML('http://music.163.com/mv?id=%s'%num)
# 	parsed = getVideo(html)
# 	print parsed

ID = raw_input("Input the MV ID: ")

url = 'http://music.163.com/mv?id=' + str(ID)

html = getHTML(url)
parsed = getVideo(html)
# print parsed
videoUrls = parsed[0].split("&")
# print videoUrls

mp4Url = videoUrls[0].strip()
print "mp4Url: " + mp4Url

trackName = videoUrls[3].split("=")[1].strip()
print "Song: " + trackName

artistName = videoUrls[4].split("=")[1].strip()
print "Artist: " + artistName

# filename = '%s/%s.mp4' % (artistName, trackName)
# print filename