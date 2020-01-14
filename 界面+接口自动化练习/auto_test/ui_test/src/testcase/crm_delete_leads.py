from selenium import webdriver
from time import sleep
import time
import unittest

class delete_leads(unittest.TestCase):
    def setUp(self):
        global chrome
        chrome = webdriver.Chrome()
        chrome.get("http://192.168.0.111/crm/index.php?m=user&a=login")
        chrome.find_element_by_name("name").send_keys("xujianda")
        chrome.find_element_by_name("password").send_keys("123456")
        chrome.find_element_by_name("submit").click()
    def test_delete_leads(self):
        """测试删除线索"""
        chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a').click()   #点击线索
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[3]/td[1]/input').click()   #选择要删除的线索
        chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/ul/li[1]/div/a').click()   #点击批量删除下拉框
        chrome.find_element_by_xpath('//*[@id="delete"]').click()     #点击批量删除
        t = chrome.switch_to.alert.text    #获取警告框中的文本
        print(t)
        chrome.switch_to.alert.accept()    #相当于警告框中的确定
        # chrome.switch_to.alert.dismiss()   #相当于警告框中的取消
        massage = chrome.find_element_by_xpath('/html/body/div[5]/div[2]').text
        self.assertEqual("删除成功!",massage[2:])
        now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        chrome.get_screenshot_as_file(r"D:\python_work\auto_test\img\\"+now+"delxs.png")
    def tearDown(self):
        #退出登录
        chrome.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a").click()
        chrome.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/ul/li[12]/a").click()
        sleep(2)
        chrome.quit()

if __name__ == '__main__':
    unittest.main()