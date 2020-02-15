#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo2.py
# Author: Helen
# Date  : 2020/2/12

from selenium import webdriver
import time
from selenium.webdriver import ActionChains


# 创建了一个叫做driver的变量 --> 浏览器驱动
driver = webdriver.Chrome()
# 自动化访问一个网页地址
driver.get('https://www.baidu.com')

# id定位  id选择器
driver.find_element_by_id('kw').send_keys('美女')

time.sleep(2)
# 使用鼠标模拟单击
ac = driver.find_element_by_id('su')
ActionChains(driver).move_to_element(ac).click(ac).perform()
