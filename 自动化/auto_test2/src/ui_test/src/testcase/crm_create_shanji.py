from selenium import webdriver
from time import sleep
import time
import  unittest    #单元测试框架
from auto_test.data.get_name import get_name

class create_product(unittest.TestCase):
    def setUp(self):
        #用户登录
        global chrome
        chrome = webdriver.Chrome()
        chrome.get("http://192.168.0.111/crm/index.php?m=user&a=login")
        chrome.find_element_by_name("name").send_keys("xujianda")
        chrome.find_element_by_name("password").send_keys("123456")
        chrome.find_element_by_name("submit").click()
    def test_add_product(self):
        """测试添加商机"""
        chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[3]/a').click()  #点击商机
        chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div/a').click()   #点击添加商机
        chrome.find_element_by_xpath('//*[@id="customer_name"]').click()    #点击客户
        sleep(1)
        chrome.find_element_by_xpath('//*[@id="datas"]/tr[6]/td[1]/input[1]').click()     #选择客户-张飞3
        chrome.find_element_by_xpath('/html/body/div[10]/div[3]/div/button[1]/span').click()   #点击确定
        # chrome.find_element_by_xpath('//*[@id="customer_name"]').send_keys("马云9")   #选择客户-马云9
        kh = get_name()
        khname = kh.get_khname()
        chrome.find_element_by_xpath('//*[@id="name"]').send_keys(khname)      #输入商机名
        chrome.find_element_by_xpath('//*[@id="origin"]').click()    #点击商机来源
        chrome.find_element_by_xpath('//*[@id="origin"]/option[3]').click()    #选择网络营销
        chrome.find_element_by_xpath('//*[@id="estimate_price"]').send_keys("230")    #输入预计成交价-230
        chrome.find_element_by_xpath('//*[@id="nextstep_time"]').send_keys("2019-01-20 16:20")      #下次联系时间
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tfoot/tr/td/input[1]').click()    #点击保存
        massage = chrome.find_element_by_xpath('/html/body/div[5]/div[2]').text
        self.assertEqual("添加商机成功！",massage[2:])
        now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        chrome.get_screenshot_as_file(r"D:\python_work\auto_test\img\\"+now+"商机.png")
    def tearDown(self):
        chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a').click()   #点击用戶名
        chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/ul/li[12]/a').click()   #点击退出
        sleep(3)
        chrome.quit()
if __name__ == '__main__':
    unittest.main()
