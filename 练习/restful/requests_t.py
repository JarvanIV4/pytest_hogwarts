# -*- coding: utf-8 -*-
# @Time : 2020/04/11
# @Author : Wind

import requests

resp = requests.get('http://127.0.0.1:5000/login', auth=('magigo', '123456'))
print(resp.text)