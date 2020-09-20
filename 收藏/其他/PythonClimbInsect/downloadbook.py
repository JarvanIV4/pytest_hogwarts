# -*- coding:utf8 -*-
import urllib2,re
from bs4 import BeautifulSoup

root = 'http://www.biquge.com/'
urlList = [];
chaptername = raw_input('请输入笔趣阁小说章节目录子地址:')
print u"正在解析章节列表..."

soup = BeautifulSoup(urllib2.urlopen(root+chaptername+u'/').read())

novelname = soup.find('div',id='info').find('h1').get_text()

for result in soup.find(id="list").find("dt").find_next("dt").find_next_siblings("dd"):
        res = result.find_next("a")
        urlList.append(res['href'])

fileHandle = open(novelname+u'.txt','a')

for result in urlList:
        temp = BeautifulSoup(urllib2.urlopen(root+result).read())
        #print temp.find(id="content").get_text()
        print u"正在下载:"+temp.title.text;
        content = temp.find(id="content").get_text().encode('gbk','ignore')
        #rstr = r'<(S*?)[^>]*>.*?|<.*? /> '
        #fileHandle.write(re.sub(rstr, "", content))
        fileHandle.write(content)
fileHandle.close()
print "~~~~~~~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#为了避免双击的时候直接一闪退出，在最后面加了这么一句
raw_input("Press <Enter> To Quit!")
