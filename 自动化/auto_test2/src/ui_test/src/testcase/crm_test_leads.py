#新建线索
from selenium import webdriver
from time import sleep
import unittest
import time
from auto_test.ui_test.src.common.common import method
from selenium.webdriver.common.by import By

class create_leads(unittest.TestCase):
    def setUp(self):
        #用户登录
        global chrome,m
        chrome = webdriver.Chrome()
        chrome.get("http://192.168.0.111/crm/index.php?m=user&a=login")
        m = method(chrome)
        m.login("xujianda","123456")
        # chrome.find_element_by_name("name").send_keys("xujianda")
        # chrome.find_element_by_name("password").send_keys("123456")
        # # sleep(3)
        # chrome.find_element_by_name("submit").click()
    def test_add_leads(self):
        """测试新建线索"""
        m.click_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a")
        #设定滚动条与页面顶端的距离
        js = "var a=document.documentElement.scrollTop=10000"
        chrome.execute_script(js)
        m.click_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/a")
        m.click_element(By.XPATH,"//*[@id='source']/option[4]")
        m.input_text(By.ID,"position","员工")
        m.input_text(By.ID,"mobile","17612345678")
        m.input_text(By.ID,"name","乐科")
        m.input_text(By.ID,"contacts_name","李先生")
        m.click_element(By.XPATH,"//*[@id='saltname']/option[2]")
        m.input_text(By.XPATH,'//*[@id="email"]',"123@qq.com")
        m.click_element(By.XPATH,"//*[@id='form1']/table/tbody/tr[6]/td[2]/select[1]/option[20]")
        m.click_element(By.XPATH,"//*[@id='form1']/table/tbody/tr[6]/td[2]/select[2]/option[4]")
        m.click_element(By.XPATH,"//*[@id='form1']/table/tbody/tr[6]/td[2]/select[3]/option[7]")
        m.input_text(By.ID,"nextstep","留言")
        m.input_text(By.XPATH,'//*[@id="description"]',"备注")
        m.click_element(By.XPATH,'//*[@id="form1"]/table/tfoot/tr/td/input[1]')
        massage = chrome.find_element_by_xpath('/html/body/div[5]/div[2]').text
        self.assertEqual("线索添加成功！",massage[2:])
        now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        chrome.get_screenshot_as_file(r"D:\python_work\auto_test\img\\"+now+"leads.png")

        # chrome.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a").click() #点击线索
        # chrome.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/a").click()  #点击新建线索
        # chrome.find_element_by_xpath("//*[@id='source']/option[4]").click()    #点击来源
        # chrome.find_element_by_id("position").send_keys("员工")
        # chrome.find_element_by_id("mobile").send_keys("17612345678")
        # chrome.find_element_by_id("name").send_keys("乐科")  #填写公司
        # chrome.find_element_by_id("contacts_name").send_keys("李先生")
        # chrome.find_element_by_xpath("//*[@id='saltname']/option[2]").click()
        # chrome.find_element_by_xpath('//*[@id="email"]').send_keys("123@qq.com")
        # chrome.find_element_by_xpath("//*[@id='form1']/table/tbody/tr[6]/td[2]/select[1]/option[20]")
        # chrome.find_element_by_xpath("//*[@id='form1']/table/tbody/tr[6]/td[2]/select[2]/option[4]")
        # chrome.find_element_by_xpath("//*[@id='form1']/table/tbody/tr[6]/td[2]/select[3]/option[7]")
        # chrome.find_element_by_id("nextstep").send_keys("留言")
        # chrome.find_element_by_xpath('//*[@id="description"]').send_keys("备注")
        # chrome.find_element_by_xpath('//*[@id="form1"]/table/tfoot/tr/td/input[1]').click()     #点击保存
        # # chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td/input[2]').click()  #点击保存并新建
        # massage = chrome.find_element_by_xpath('/html/body/div[5]/div[2]').text
        # self.assertEqual("线索添加成功！",massage[2:])
        # now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        # chrome.get_screenshot_as_file(r"D:\python_work\auto_test\img\\"+now+"leads.png")
    def tearDown(self):
        #退出登录
        m.logout()

if __name__ == '__main__':
    unittest.main()
