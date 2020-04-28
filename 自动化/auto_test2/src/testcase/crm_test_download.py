#导出线索，下载文件
from selenium import webdriver
from time import sleep
import time
import unittest

class crm_download(unittest.TestCase):
    def setUp(self):
        #
        option = webdriver.ChromeOptions()
        prefs = {
            'profiile.default_content_settings.popups':0,
            'download.default_directory':'D:\\html'}
        option.add_experimental_option('prefs',prefs)
        global chrome
        chrome = webdriver.Chrome(chrome_options=option)
        chrome.get("http://192.168.0.111/crm/index.php?m=user&a=login")
        chrome.find_element_by_name("name").send_keys("xujianda")
        chrome.find_element_by_name("password").send_keys("123456")
        chrome.find_element_by_name("submit").click()
    def test_download_leads(self):
        """测试导出线索"""
        chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a').click()     #点击线索
        chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div/div/button').click()    #点击线索工具
        chrome.find_element_by_xpath('//*[@id="excelExport"]').click()      #点击导出线索
        chrome.switch_to.alert.accept()    #点击提示框中确定
        now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        chrome.get_screenshot_as_file(r"D:\python_work\auto_test\img\\"+now+"download.png")
    def tearDown(self):
            #退出登录
        chrome.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a").click()
        chrome.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/ul/li[12]/a").click()
        sleep(3)
        chrome.quit()


