# -*- coding: utf-8 -*-
# __author__: Wind
# 2020/9/20 21:14
import requests
import urllib3

session = requests.session()
session.keep_alive = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 关闭安全请求警告


class HttpAPI:
    headers = {"Content-Type": "application/json"}

    def send_post(self, url, data=None, headers=headers, **kwargs):
        response = session.post(url=url, data=data, headers=headers, verify=False, **kwargs)
        return response

    def send_get(self, url, params=None, headers=None):
        response = session.get(url=url, params=params, headers=headers, verify=False)
        return response


