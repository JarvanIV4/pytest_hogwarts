from time import sleep
from auto_test.ui_test.src.common.common import method
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2345手机号码搜索
class mobile(unittest.TestCase):

    def setUp(self):
        global driver,m
        chrome = webdriver.Chrome()
        chrome.get("https://tools.2345.com")
        m = method(chrome)
        sleep(2)

    def test_mobile(self):

        m.input_text(By.XPATH,'//*[@id="mobile"]',"15012345678")
        m.locate_element('//*[@id="shouji"]/input[2]')
        # self.input_text('//*[@id="mobile"]',"15012345678")      # 输入手机号码
        # self.click_ele('//*[@id="shouji"]/input[2]')        # 点击搜索
        # self.driver.switch_to.window(self.driver.window_handles[1])     # 切换到第二个网页
        # self.click_ele('//*[@id="mobileform"]/div/div/input[2]')        # 点击搜索
        # message = self.locate_text('/html/body/div[2]/div[3]/div[2]/div/div/div[1]/div/p[2]/strong')
        # self.assertEqual("云南省昭通市",message,"测试不通过")
        # sleep(5)
        # self.screenshot()


    def tearDown(self):
        sleep(5)

if __name__ == '__main__':
    unittest.main()

