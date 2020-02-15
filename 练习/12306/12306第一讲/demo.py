#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo.py
# Author: Helen
# Date  : 2020/2/12

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 创建了一个叫做driver的变量 --> 浏览器驱动
driver = webdriver.Chrome(executable_path="chromedriver.exe")
# 自动化访问一个网页地址
driver.get('https://www.baidu.com')
# id定位  id选择器
driver.find_element_by_id('kw').send_keys('美女')
# name 定位 名称
# driver.find_element_by_name('wd')
# class 定位 类选择器
# driver.find_element_by_class_name('s_ipt')

time.sleep(2)
# 点击百度一下
# driver.find_element_by_id('su').click()

# 自动化程序模拟键盘回车操作
# driver.find_element_by_id('kw').send_keys(Keys.ENTER)

time.sleep(2)
# 网页快照
# driver.save_screenshot('123.png')

# 获取网页的源代码
# print(driver.page_source)

# 在一个网页当中 全选输入框内容 ctrl + a
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')

# 剪切
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, Keys.ALT, 'x')




