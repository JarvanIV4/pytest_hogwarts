#添加供应商
from selenium import webdriver
from time import sleep
from auto_test.ui_test.src.common.common import method
from selenium.webdriver.common.by import By
import unittest

class oa_create_gys(unittest.TestCase):

    def setUp(self):
        global chrome,m
        chrome = webdriver.Chrome()
        chrome.get("http://192.168.0.110/ranzhi/www/sys/user-login")
        m = method(chrome)
        m.login_oa("xujianda","123456")
        # chrome.find_element_by_xpath('//*[@id="account"]').send_keys("xujianda")
        # chrome.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
        # chrome.find_element_by_xpath('//*[@id="submit"]').click()

    def test_add_gys(self):
        """添加供应商"""
        m.click_element(By.XPATH,'//*[@id="s-menu-1"]/button/img')   #点击客户管理
        chrome.switch_to.frame("iframe-1")      #切換到iframe-1
        m.click_element(By.XPATH,'//*[@id="mainNavbar"]/ul/li[5]/a')    #点击供应商
        m.click_element(By.XPATH,'//*[@id="menuActions"]/a')    #点击新建供应商
        m.input_text(By.XPATH,'//*[@id="name"]',"供应商")    #输入名称
        m.input_text(By.XPATH,'//*[@id="contact"]',"联系人")  #输入联系人
        m.input_text(By.XPATH,'//*[@id="phone"]',"17612345678")     #输入电话
        chrome.find_element_by_xpath('//*[@id="email"]').send_keys("123321@qq.com")     #输入电子邮箱
        chrome.find_element_by_xpath('//*[@id="qq"]').send_keys("123456110")      #输入QQ号码
        chrome.find_element_by_xpath('//*[@id="type"]').click()    #点击类型
        chrome.find_element_by_xpath('//*[@id="type"]/option[2]').click()     #选择国有企业
        chrome.find_element_by_xpath('//*[@id="size"]').click()   #选择规模
        chrome.find_element_by_xpath('//*[@id="size"]/option[2]').click()    #选择100人以上
        chrome.find_element_by_xpath('//*[@id="weixin"]').send_keys("123")    #输入微信号
        chrome.find_element_by_xpath('//*[@id="site"]').send_keys("www.baidu.com")    #输入网址
        # chrome.switch_to.default_content()
        frame = chrome.find_element_by_xpath(r'//*[@id="providerForm"]/table/tbody/tr[14]/td/div/div[2]/iframe')
        chrome.switch_to.frame(frame)
        # chrome.find_element_by_xpath('//*[@id="providerForm"]/table/tbody/tr[14]/td/div/div[2]/textarea').send_keys("简介")   #输入简介
        chrome.find_element_by_xpath('/html/body').send_keys("简介")
        chrome.switch_to.parent_frame()
        # chrome.switch_to.default_content()
        # chrome.switch_to.frame("iframe-1")      #切換到iframe-1
        chrome.find_element_by_xpath('//*[@id="submit"]').click()    #点击保存


        # chrome.find_element_by_xpath('//*[@id="s-menu-1"]/button/img').click()    #点击客户管理
        # chrome.switch_to.frame("iframe-1")      #切換到iframe-1
        # chrome.find_element_by_xpath('//*[@id="mainNavbar"]/ul/li[5]/a').click()    #点击供应商
        # chrome.find_element_by_xpath('//*[@id="menuActions"]/a').click()     #点击新建供应商
        # chrome.find_element_by_xpath('//*[@id="name"]').send_keys("供应商")     #输入名称
        # chrome.find_element_by_xpath('//*[@id="contact"]').send_keys("联系人")    #输入联系人
        # chrome.find_element_by_xpath('//*[@id="phone"]').send_keys("17612345678")     #输入电话
        # chrome.find_element_by_xpath('//*[@id="email"]').send_keys("123321@qq.com")     #输入电子邮箱
        # chrome.find_element_by_xpath('//*[@id="qq"]').send_keys("123456110")      #输入QQ号码
        # chrome.find_element_by_xpath('//*[@id="type"]').click()    #点击类型
        # chrome.find_element_by_xpath('//*[@id="type"]/option[2]').click()     #选择国有企业
        # chrome.find_element_by_xpath('//*[@id="size"]').click()   #选择规模
        # chrome.find_element_by_xpath('//*[@id="size"]/option[2]').click()    #选择100人以上
        # chrome.find_element_by_xpath('//*[@id="weixin"]').send_keys("123")    #输入微信号
        # chrome.find_element_by_xpath('//*[@id="site"]').send_keys("www.baidu.com")    #输入网址
        # # chrome.switch_to.default_content()
        # frame = chrome.find_element_by_xpath(r'//*[@id="providerForm"]/table/tbody/tr[14]/td/div/div[2]/iframe')
        # chrome.switch_to.frame(frame)
        # # chrome.find_element_by_xpath('//*[@id="providerForm"]/table/tbody/tr[14]/td/div/div[2]/textarea').send_keys("简介")   #输入简介
        # chrome.find_element_by_xpath('/html/body').send_keys("简介")
        # chrome.switch_to.parent_frame()
        # # chrome.switch_to.default_content()
        # # chrome.switch_to.frame("iframe-1")      #切換到iframe-1
        # chrome.find_element_by_xpath('//*[@id="submit"]').click()    #点击保存

    def tearDown(self):
        m.logout_oa()





