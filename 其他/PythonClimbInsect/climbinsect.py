# -*- coding:GBK -*-

from bs4 import BeautifulSoup
import os, sys, urllib2,time,random,re

#首先创建文件夹，提示输入，在当前目录创建
try:
    foldname = raw_input('请输入文件夹名称:')
    path = os.getcwd()
    new_path = os.path.join(path,foldname)
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    choice = raw_input('你想用当前时间定义图片名吗?(Y/N):')
except Exception, e:
    print e
    
#定义函数，读取URL中标签的img并存储到文件夹中
def getHtmlImg(page = 1):
    #从TXT中读取第一行的数据，获取url
    try:
        urlfile = open('URL.txt')
        url = urlfile.readline().strip('\n') % page
        classname = urlfile.readline().strip('\n')

        content = urllib2.urlopen(url)
        soup = BeautifulSoup(content)

        my_div = soup.find_all('div',class_=classname)
        for div in my_div:
            imgs = div.find_all('img')
            for img in imgs:
                link = img.get('src')
                print link
                content2 = urllib2.urlopen(link).read()

                if choice == u'y' or choice == u'Y':
                    with open(new_path+'/'+time.strftime('%H-%M-%S')+random.choice('qwertyuiopasdfghjklzxcvbnm')+link[-5:],'wb') as code:
                        code.write(content2)
                else:
                    #根据获取的图片路径，把图片存到文件夹中
                    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/\:*?"<>|'
                    new_title = re.sub(rstr, "", link[-11:])

                    with open(new_path+'/'+new_title,'wb') as code:
                        code.write(content2)

        page = int(page)+1
        print u'开始抓取下一页中的图片'
        print '第 %s 页' % page
        getHtmlImg(page)
    except Exception, e:
        print e

        
getHtmlImg()



print "~~~~~~~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#为了避免双击的时候直接一闪退出，在最后面加了这么一句
raw_input("Press <Enter> To Quit!")
