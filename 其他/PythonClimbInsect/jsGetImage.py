#-*-coding:utf-8-*-      
  
# 进行表单提交  小项  2008-10-09      
 
import httplib,urllib;  #加载模块      

#定义需要进行发送的数据      
params = urllib.urlencode('')       
#定义一些文件头      
##headers = {"Accept":"image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5",
##           "Referer":"http://www.imanhua.com/comic/76/list_75983.html",
##           "Accept-Language":"zh-CN",
##           "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
##           "Accept-Encoding":"gzip, deflate",
##           "Host":"t6.mangafiles.com",
##           "If-Modified-Since":"Wed, 05 Dec 2012 16:00:00 GMT",
##           "If-None-Match":"0404b941d3cd1:0",
##           "Connection":"Keep-Alive"};
headers = {"Accept":"image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5",
           "Referer":"http://www.imanhua.com/comic/76/list_59262.html",
           "Accept-Language":"zh-CN",
           "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
           "Accept-Encoding":"gzip, deflate",
           "Host":"t6.mangafiles.com",
           "Connection":"Keep-Alive"}; 
#与网站构建一个连接
conn = httplib.HTTPConnection("www.imanhua.com",80, False);       
#开始进行数据提交   同时也可以使用get进行
imgurl = 'http://t6.mangafiles.com/Files/Images/76/75983/001.png'
newurl = imgurl[24:]
conn.request(method="GET",url="/Files/Images/76/59262/imanhua_001.jpg",body=params,headers=headers)
#返回处理后的数据      
response = conn.getresponse();  
#判断是否提交成功      
if response.status == 304:  
    print "发布成功!^_^!";       
else:       
    print "发布失败\^0^/";
html = response.read()
print response.status,response.reason
print html
with open(u'aa'+'/'+u'001.jpg','wb') as code:
    code.write(html)
conn.close();    


import urllib2
req = urllib2.Request('http://t6.mangafiles.com/Files/Images/76/75983/001.png')
req.add_header('Referer', 'http://www.imanhua.com/comic/76/list_59262.html')
content = urllib2.urlopen(req).read()
print content
with open(u'aa'+'/'+u'002.jpg','wb') as code:
    code.write(content)
