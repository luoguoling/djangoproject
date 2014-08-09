__author__ = 'rolin'
#coding:utf-8
import urllib,sys,time
from time import sleep
def cbk(a,b,c):
	"""
	@a:已经下载的数据块
	@b:数据块的大小
	@c:远程文件大小
	"""
	output = sys.stdout
	per = 100.0*a*b / c
	# for count in range(1,100):
	# 	second =1
	# 	sleep(second)
	# 	output.write('\r%d\r' % count)
	# 	output.flush()

	print '%.2f%%' % per
	if per > 100:
		per = 100

		if per == 100:
			print "the download is successful"
		else:
			print "the download is fail"
url = 'http://120.138.75.88/download/ncftp-3.2.3-1.2.x86_64.rpm'
local = 'd:\\ncftp-3.2.3-1.2.x86_64.rpm'
urllib.urlretrieve(url, local, cbk)
