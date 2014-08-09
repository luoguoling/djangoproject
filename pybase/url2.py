#coding:utf-8
__author__ = 'rolin'
import urllib
def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per

    print '\rFileSize: %d   Already download %d KB(%.2f ' %(a,b/1024,per)+'%)'
    if per == 100:
		print "download is successful"



url = 'http://120.138.75.88/download/ncftp-3.2.3-1.2.x86_64.rpm'
local = 'd:\\ncftp-3.2.3-1.2.x86_64.rpm'
urllib.urlretrieve(url, local, cbk)