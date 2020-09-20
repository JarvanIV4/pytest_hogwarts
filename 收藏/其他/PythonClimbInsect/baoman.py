# -*- coding:utf8 -*-
# 2013.12.36 19:41 wnlo-c209
# 抓取dbmei.com的图片。

from bs4 import BeautifulSoup
import os, sys, urllib2,time,random

# 创建文件夹，昨天刚学会
path = os.getcwd()   				     # 获取此脚本所在目录
new_path = os.path.join(path,u'暴走漫画')
if not os.path.isdir(new_path):
	os.mkdir(new_path)


def page_loop(page=1):
	url = 'http://baozoumanhua.com/all/hot/page/%s?sv=1389537379' % page
	content = urllib2.urlopen(url)
	soup = BeautifulSoup(content)

	my_girl = soup.find_all('div',class_='img-wrap')
	for girl in my_girl:
		jokes = girl.find('img')
		link = jokes.get('src')
		flink = link
		print flink
		content2 = urllib2.urlopen(flink).read()

		#with open(u'暴走漫画'+'/'+time.strftime('%H-%M-%S')+random.choice('qwertyuiopasdfghjklzxcvbnm')+flink[-5:],'wb') as code:          #在OSC上现学的
		with open(u'暴走漫画'+'/'+flink[-11:],'wb') as code:
			code.write(content2)

	page = int(page) + 1
	print u'开始抓取下一页'
	print 'the %s page' % page
	page_loop(page)
	
page_loop()
print "~~~~~~~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#为了避免双击的时候直接一闪退出，在最后面加了这么一句
raw_input("Press <Enter> To Quit!")
