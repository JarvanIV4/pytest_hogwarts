#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 爬虫补充.py
# Author: MuNian
# Date  : 2020/2/12

import requests

# 浏览器页面的url 地址
urls = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# 请求的数据接口的 地址
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false'

headers = {
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python'
}

# response = requests.post(url, headers=headers, data=data).text
# print(response)

s = requests.session()
cookie = s.get(url=urls, headers=headers)
cookies = cookie.cookies

response = s.post(url=url, headers=headers, cookies=cookies, data=data).json()
print(response)

