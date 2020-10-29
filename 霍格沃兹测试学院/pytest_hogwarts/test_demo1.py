# -*- coding: utf-8 -*-
# __author__: Wind
# 2020/10/22 20:38
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testdemo():

    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("http://ceshiren.com")
        self.driver.find_element_by_xpath()
        sleep(3)
