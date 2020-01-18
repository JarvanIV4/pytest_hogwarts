#CRM用户登录
from selenium import webdriver
from time import sleep
from auto_test.ui_test.src.common.common import method
import time
import unittest   #单元测试框架

class user_login(unittest.TestCase):
    def setUp(self):
        #测试用例的准备部分
        global chrome
        chrome = webdriver.Chrome()
        chrome.get("http://192.168.0.111/crm/index.php?m=user&a=login")
    def test_login(self):
        """测试用户登录"""
        m = method(chrome)
        m.login("xujianda","123456")
        # chrome.find_element_by_name("name").send_keys("xujianda")
        # chrome.find_element_by_name("password").send_keys("123456")
        # chrome.find_element_by_name("submit").click()
        massage = chrome.find_element_by_xpath('/html/body/div[5]/div[2]').text
        self.assertEqual("登录成功",massage[2:])
        print(massage[2:])
        now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        chrome.get_screenshot_as_file(r"D:\python_work\auto_test\img\\"+now+"login.png")
    def tearDown(self):
        #测试用例的退出部分
        chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a').click()   #点击用戶名
        chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/ul/li[12]/a').click()   #点击退出
        sleep(2)
        chrome.quit()

if __name__ == '__main__':
    unittest.main()


# chrome.maximize_window()

# input = chrome.find_elements_by_class_name("text-input")
# input[0].send_keys("admin")
# input[1].send_keys("admin123")

# input = chrome.find_elements_by_tag_name("input")
# input[0].send_keys("admin")
# input[1].send_keys("admin123")
# input[2].click()
# input[3].click()


#
# name = chrome.find_element_by_xpath('/html/body/div[5]/div[3]/div[1]/div/div[1]/div[2]/p[1]').text
# print(name)
# class1 = chrome.find_element_by_xpath('/html/body/div[5]/div[3]/div[1]/div/div[1]/div[2]/p[1]').get_attribute("class")
# print(class1)


