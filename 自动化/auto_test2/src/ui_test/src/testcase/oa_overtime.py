"""申请加班"""
from selenium import webdriver
from auto_test.ui_test.src.common.common import method
from auto_test.ui_test.src.common.log import log
from selenium.webdriver.common.by import By
from time import sleep
import time
import unittest

class oa_overtime(unittest.TestCase):

    def setUp(self):
        global chrome,m
        chrome = webdriver.Chrome()
        chrome.get("http://192.168.0.110/ranzhi/www/sys/user-login")
        m = method(chrome)
        m.login_oa("xujianda","123456")
    def test_overtime(self):
        """测试申请加班"""
        m.click_element(By.XPATH,'//*[@id="s-menu-2"]/button/img')     #点击日常办公
        chrome.switch_to.frame("iframe-2")
        m.click_element(By.XPATH,'//*[@id="mainNavbar"]/ul/li[7]/a')        #点击加班
        m.click_element(By.XPATH,'//*[@id="menuActions"]/a[2]')     #点击申请加班
        m.click_element(By.XPATH,'//*[@id="typetime"]')              #点击类型（工作日加班）
        m.input_text(By.ID,"begin","2019-01-30")    #输入开始日期
        m.input_text(By.ID,"start","10:20")         #输入开始时间
        m.input_text(By.ID,"end","2019-01-31")      #输入结束日期
        m.input_text(By.ID,"finish","17:20")        #输入结束时间
        m.click_element(By.ID,"submit")         #点击保存
        sleep(5)
        message = chrome.find_element_by_xpath('//*[@id="overtimeTable"]/tbody/tr[1]/td[5]').text
        # print(message)
        self.assertEqual("2019-01-30 10:20",message)
        chrome.switch_to.default_content()
        now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        chrome.get_screenshot_as_file(r"D:\python_work\auto_test\img\\"+now+"overtime.png")
    def tearDown(self):
        m.logout_oa()



