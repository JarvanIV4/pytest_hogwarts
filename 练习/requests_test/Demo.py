# -*- coding: utf-8 -*-
# @Time : 2020/8/13
# @Author : Wind
import requests


class TestDemo:

    def test_get(self):
        r = requests.get('https://httpbin.testing-stduio.com/get')
        print(r.status_code)
        print(r.text)
        assert r.status_code == 200