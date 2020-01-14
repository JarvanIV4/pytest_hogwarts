#申请请假
from selenium import webdriver
from time import sleep
from auto_test.ui_test.src.common.common import method
import unittest

class oa_qingjia(unittest.TestCase):
    def setUp(self):
        #
        chrome = webdriver.Chrome()
        chrome.get("http://192.168.0.110/ranzhi/www/sys/user-login")
        m = method(chrome)
        m.login_oa("xujianda","123456")
        # chrome.find_element_by_xpath('//*[@id="account"]').send_keys("xujianda")
        # chrome.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
        # chrome.find_element_by_xpath('//*[@id="submit"]').click()
        sleep(2)

    def test_qingjia(self):
        chrome.find_element_by_xpath('//*[@id="s-menu-2"]/button').click()    #点击日常办公
        chrome.switch_to.frame("iframe-2")     #切换到iframe-2中
        chrome.find_element_by_xpath('//*[@id="mainNavbar"]/ul/li[5]/a').click()  #点击请假
        chrome.find_element_by_xpath('//*[@id="menuActions"]/a[2]').click()    #点击申请请假
        sleep(1)
        chrome.find_element_by_xpath('//*[@id="ajaxForm"]/table/tbody/tr[1]/td[1]/label[4]').click()     #类型选择年假
        # chrome.find_element_by_xpath('//*[@id="begin"]').click()     #点击开始日期
        # chrome.find_element_by_xpath('/html/body/div[5]/div[3]/table/tbody/tr[3]/td[5]').click()   #选择开始日期
        chrome.find_element_by_xpath('//*[@id="begin"]').clear()
        chrome.find_element_by_xpath('//*[@id="begin"]').send_keys("2019-01-12")      #输入开始日期
        chrome.find_element_by_xpath('//*[@id="start"]').clear()
        chrome.find_element_by_xpath('//*[@id="start"]').send_keys("10:40")
        # chrome.find_element_by_xpath('//*[@id="start"]').click()     #点击开始时间
        # chrome.find_element_by_xpath('/html/body/div[7]/div[2]/table/tbody/tr/td/span[11]')   #选择开始时间为9:00
        # chrome.find_element_by_xpath('/html/body/div[7]/div[1]/table/tbody/tr/td/span[7]')   #选择开始时间为9:30
        chrome.find_element_by_xpath('//*[@id="end"]').send_keys("2019-01-13")      #输入结束日期
        chrome.find_element_by_xpath('//*[@id="finish"]').clear()
        chrome.find_element_by_xpath('//*[@id="finish"]').send_keys("18:40")   #输入结束时间为18:40
        # chrome.find_element_by_xpath('//*[@id="hours"]').send_keys("5")     #输入总时长
        chrome.find_element_by_xpath('//*[@id="desc"]').send_keys("事由")   #输入事由
        chrome.find_element_by_xpath('//*[@id="submit"]').click()      #点击保存
        sleep(2)
        chrome.quit()

