__author__ = 'Administrator'
import requests,urllib2
print "downloading with requests"
url = "http://120.138.75.88/download/resource.tar.gz"
try:
	f = urllib2.urlopen(url)
	with open('resource.tar.gz','wb') as code:
		code.write(f.read())
except:
	print "the file can not download"
