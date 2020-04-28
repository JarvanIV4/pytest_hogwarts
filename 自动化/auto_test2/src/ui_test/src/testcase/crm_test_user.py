#新建用户
from selenium import webdriver
from time import sleep
import unittest
import time
from auto_test.data.get_name import get_name

class create_user(unittest.TestCase):
    def setUp(self):
        global chrome
        chrome = webdriver.Chrome()
        chrome.get("http://192.168.0.111/crm/index.php?m=user&a=login")
        chrome.find_element_by_name("name").send_keys("admin")
        chrome.find_element_by_name("password").send_keys("admin123")
        chrome.find_element_by_name("submit").click()
    def test_add_user(self):
        """测试添加用户"""
        chrome.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a").click()
        chrome.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/ul/li[4]/a").click()
        chrome.find_element_by_xpath("//*[@id='user_form']/div[1]/div/a[3]").click()
        # chrome.find_element_by_xpath("//*[@id='name'']").send_keys("leke123")
        user = get_name()
        username = user.get_khname()
        chrome.find_element_by_css_selector('table.table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)').send_keys(username)
        chrome.find_element_by_xpath("//*[@id='password']").send_keys("123")
        chrome.find_element_by_css_selector('table.table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > select:nth-child(1) > option:nth-child(2)').click()
        chrome.find_element_by_css_selector("#department2 > option:nth-child(2)").click()
        chrome.find_element_by_css_selector("#role2 > option:nth-child(1)").click()
        chrome.find_element_by_css_selector('table.table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(2) > input:nth-child(1)').click()    #点击添加
        # chrome.find_element_by_css_selector("table.table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(2) > input:nth-child(2)").click()
        massage = chrome.find_element_by_xpath('/html/body/div[5]/div[2]').text
        self.assertEqual("添加成功，该用户已可以登录系统!",massage[2:])
        now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        chrome.get_screenshot_as_file(r"D:\python_work\auto_test\img\\"+now+"user.png")
    def tearDown(self):
        #退出登录
        chrome.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a").click()
        chrome.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/ul/li[12]/a").click()
        sleep(3)
        chrome.quit()

if __name__ == '__main__':
    unittest.main()