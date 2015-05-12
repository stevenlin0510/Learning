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

ID = raw_input("Input the MV ID: ")
url = 'http://music.163.com/mv?id=' + str(ID)

html = getHTML(url)
parsed = getVideo(html)
videoUrls = parsed[0].split("&")
mp4Url = videoUrls[0].strip()
trackName = videoUrls[3].split("=")[1].strip()
artistName = videoUrls[4].split("=")[1].strip()

print "mp4Url: " + mp4Url + '\n' + "Song: " + trackName + '\n' + "Artist: " + artistName
 
# filename = '%s/%s.mp4' % (artistName, trackName)
