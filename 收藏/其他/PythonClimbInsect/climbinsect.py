# -*- coding:GBK -*-

from bs4 import BeautifulSoup
import os, sys, urllib2,time,random,re

#���ȴ����ļ��У���ʾ���룬�ڵ�ǰĿ¼����
try:
    foldname = raw_input('�������ļ�������:')
    path = os.getcwd()
    new_path = os.path.join(path,foldname)
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    choice = raw_input('�����õ�ǰʱ�䶨��ͼƬ����?(Y/N):')
except Exception, e:
    print e
    
#���庯������ȡURL�б�ǩ��img���洢���ļ�����
def getHtmlImg(page = 1):
    #��TXT�ж�ȡ��һ�е����ݣ���ȡurl
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
                    #���ݻ�ȡ��ͼƬ·������ͼƬ�浽�ļ�����
                    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/\:*?"<>|'
                    new_title = re.sub(rstr, "", link[-11:])

                    with open(new_path+'/'+new_title,'wb') as code:
                        code.write(content2)

        page = int(page)+1
        print u'��ʼץȡ��һҳ�е�ͼƬ'
        print '�� %s ҳ' % page
        getHtmlImg(page)
    except Exception, e:
        print e

        
getHtmlImg()



print "~~~~~~~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#Ϊ�˱���˫����ʱ��ֱ��һ���˳���������������ôһ��
raw_input("Press <Enter> To Quit!")
