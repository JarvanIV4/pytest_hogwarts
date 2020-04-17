import requests
import os


def spider_baidu():
    """爬取百度"""
    url = 'https://www.baidu.com'
    kv = {'wd': 'python'}
    try:
        r = requests.get(url, params=kv)
        r.raise_for_status()
        print(r.text[:1000])
    except:
        print('爬取失败')


if __name__ == '__main__':
    spider_baidu()