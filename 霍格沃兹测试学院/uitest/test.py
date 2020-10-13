# -*- coding: utf-8 -*-
# __author__: Wind
# 2020/10/13 22:16
from selenium import webdriver


def test_baidu():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")


if __name__ == '__main__':
    test_baidu()