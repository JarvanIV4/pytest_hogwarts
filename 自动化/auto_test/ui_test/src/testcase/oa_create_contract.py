#创建合同
from selenium import webdriver
from time import sleep
from auto_test.ui_test.src.common.common import method
from selenium.webdriver.common.by import By
import unittest
import os

class contract(unittest.TestCase):
    def setUp(self):
        global chrome,m
        chrome = webdriver.Chrome()
        chrome.get("http://192.168.0.110/ranzhi/www/sys/user-login")
        m = method(chrome)
        m.login_oa("xujianda","123456")
        # chrome.find_element_by_xpath('//*[@id="account"]').send_keys("xujianda")
        # chrome.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
        # chrome.find_element_by_xpath('//*[@id="submit"]').click()
        # sleep(1)
    def test_add_contract(self):
        m.click_element(By.XPATH,'//*[@id="s-menu-1"]/button/img')    #点击客户管理
        chrome.switch_to.frame("iframe-1")   #切换到iframe-1表单
        m.click_element(By.XPATH,'//*[@id="mainNavbar"]/ul/li[3]/a')    #点击合同
        m.click_element(By.XPATH,'//*[@id="menuActions"]/a')    #点击新建合同
        m.click_element(By.XPATH,'//*[@id="customer_chosen"]')  #点击所属客户
        m.click_element(By.XPATH,'//*[@id="customer_chosen"]/div/ul/li[1]')     #选择第一个所属客户
        m.click_element(By.XPATH,'//*[@id="orderTD"]/div/span[1]/select')       #点击签约订单
        m.click_element(By.XPATH,'//*[@id="orderTD"]/div/span[1]/select/option[2]')    #选择第一个订单
        m.input_text(By.NAME,"name","abc")
        m.input_text(By.XPATH,'//*[@id="code"]',"123")  #输入合同编号
        m.click_element(By.XPATH,'//*[@id="currency"]')   #点击金额
        m.click_element(By.XPATH,'//*[@id="currency"]/option[2]')   #选择美元
        m.input_text(By.XPATH,'//*[@id="amount"]',"500")   ##输入金额500
        m.click_element(By.XPATH,'//*[@id="fileBox1"]/tbody/tr/td[1]/div/input')    #点击选择文件
        os.chdir(r"D:\python_work\autoit")
        os.system("upload.exe")
        m.input_text(By.XPATH,'//*[@id="customer_chosen"]/div/ul/li[1]',"sss")
        m.click_element(By.XPATH,'//*[@id="submit"]')  #点击完成

    def tearDown(self):
        m.logout_oa()


# chrome.find_element_by_xpath('//*[@id="s-menu-1"]/button/img').click()    #点击客户管理
# # chrome.find_element_by_xpath('//*[@id="mainNavbar"]/div/ul[2]/li[5]/a').click()   #点击合同
# # chrome.switch_to.frame('iframe-dashboard')    #切换到iframe-dashboard表单
# # chrome.find_element_by_xpath('//*[@id="menuActions"]/a').click()     #点击创建合同
# chrome.switch_to.frame("iframe-1")   #切换到iframe-1表单
# chrome.find_element_by_xpath('//*[@id="mainNavbar"]/ul/li[3]/a').click()   #点击合同
# chrome.find_element_by_xpath('//*[@id="menuActions"]/a').click()   #点击新建合同
# chrome.find_element_by_xpath('//*[@id="customer_chosen"]').click()    #点击所属客户
# chrome.find_element_by_xpath('//*[@id="customer_chosen"]/div/ul/li[1]').click()         #选择第一个所属客户
# sleep(2)
# chrome.find_element_by_xpath('//*[@id="orderTD"]/div/span[1]/select').click()      #点击签约订单
# chrome.find_element_by_xpath('//*[@id="orderTD"]/div/span[1]/select/option[2]').click()   #选择第一个订单
# chrome.find_element_by_xpath('//*[@id="code"]').send_keys("123")     #输入合同编号
# chrome.find_element_by_xpath('//*[@id="currency"]').click()     #点击金额
# chrome.find_element_by_xpath('//*[@id="currency"]/option[2]').click()     #选择美元
# chrome.find_element_by_xpath('//*[@id="amount"]').clear()    #清空金额
# chrome.find_element_by_xpath('//*[@id="amount"]').send_keys("500")   #输入金额500
# chrome.find_element_by_xpath('//*[@id="contact"]').click()     #点击联系人
# chrome.find_element_by_xpath('//*[@id="contact"]/option[2]').click()    #选择联系人莜莜
# chrome.find_element_by_xpath('//*[@id="ajaxForm"]/table/tbody/tr[8]/td/div/span').click()    #点击新建合同地址
# chrome.find_element_by_xpath('//*[@id="newAddress"]').send_keys("合同地址")       #输入合同地址
# chrome.find_element_by_xpath('//*[@id="signedBy_chosen"]/a').click()      #点击由谁签署
# sleep(1)
# chrome.find_element_by_xpath('//*[@id="signedBy_chosen"]/div/ul/li[6]').click()    #选择bb
# chrome.find_element_by_xpath('//*[@id="signedDate"]').click()        #选择签署日期
# chrome.find_element_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr[3]/td[6]')   #选择签署日期1月19号
# chrome.find_element_by_xpath('//*[@id="begin"]').click()       #点击开始日期
# chrome.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr[3]/td[6]').click()     #选择开始日期1月19号
# chrome.find_element_by_xpath('//*[@id="end"]').click()    #点击结束日期
# chrome.find_element_by_xpath('/html/body/div[4]/div[3]/table/tbody/tr[4]/td[4]').click()    #选择结束日期
# chrome.find_element_by_xpath('//*[@id="handlers_chosen"]/ul').click()    #点击贡献者
# chrome.find_element_by_xpath('//*[@id="handlers_chosen"]/div/ul/li[6]').click()    #选择贡献者Eden
# ajaxForm = chrome.find_element_by_xpath('//*[@id="ajaxForm"]/table/tbody/tr[13]/td/div/div[2]/iframe')
# chrome.switch_to.frame(ajaxForm)    #切换到ajaxForm
# chrome.find_element_by_xpath('/html/body').send_keys("主要条款")      #输入主要条款
# chrome.switch_to.parent_frame()
# # chrome.switch_to.default_content()
# # chrome.switch_to.frame("iframe-1")   #切换到iframe-1表单
# # chrome.find_element_by_css_selector('#fileBox1 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)').click()
# # chrome.find_element_by_xpath('//*[@id="fileBox1"]/tbody/tr/td[1]/div/input').send_keys(r"D:\html\img\2.docx")
# # chrome.find_element_by_xpath('//*[@id="fileBox1"]/tbody/tr/td[2]/div/input').send_keys(r"D:\html\img\2.docx")
# chrome.find_element_by_xpath('//*[@id="fileBox1"]/tbody/tr/td[1]/div/input').click()  #点击选择文件
# os.chdir(r"D:\python_work\autoit")
# os.system("upload.exe")
# chrome.find_element_by_xpath('//*[@id="customer_chosen"]/div/ul/li[1]').send_keys("sss")
# chrome.find_element_by_xpath('//*[@id="submit"]').click()   #点击完成
#
# sleep(5)
# chrome.quit()


