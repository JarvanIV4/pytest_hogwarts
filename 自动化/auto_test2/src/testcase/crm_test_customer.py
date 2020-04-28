#创建客户
from selenium import webdriver
from time import sleep
import time
import unittest
from auto_test.data.get_name import get_name

class create_customer(unittest.TestCase):
    def setUp(self):
        #用户登录
        global chrome
        chrome = webdriver.Chrome()
        chrome.get("http://192.168.0.111/crm/index.php?m=user&a=login")
        chrome.find_element_by_name("name").send_keys("xujianda")
        chrome.find_element_by_name("password").send_keys("123456")
        chrome.find_element_by_name("submit").click()
    def test_add_customer(self):
        """测试创建客户"""
        chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[2]/a').click()  #点击客户
        chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div/a').click()   #点击新建客户
        chrome.find_element_by_xpath('//*[@id="owner_name"]').clear()   #清除默认负责人
        chrome.find_element_by_xpath('//*[@id="owner_name"]').send_keys("xujianda")   #点击负责人
        kh = get_name()
        khname = kh.get_khname()
        chrome.find_element_by_xpath('//*[@id="name"]').send_keys(khname)   #输入客户名称
        print(khname)
        chrome.find_element_by_xpath('//*[@id="industry"]/option[3]').click()  #点击客户行业为电子商务
        chrome.find_element_by_xpath('//*[@id="origin"]/option[3]').click()    #点击客户信息来源为网络营销
        chrome.find_element_by_xpath('//*[@id="ownership1"]').click()    #选择公司性质为国企
        chrome.find_element_by_xpath('//*[@id="zip_code"]').send_keys("123456")  #输入邮编
        chrome.find_element_by_xpath('//*[@id="annual_revenue"]/option[2]').click()   #选择年营业额为1-10万
        chrome.find_element_by_xpath('//*[@id="rating2"]').click()     #选择评分为三星
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[6]/td[2]/select[1]/option[20]').click()    #选择广东省
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[6]/td[2]/select[2]/option[4]').click()     #选择深圳市
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[6]/td[2]/select[3]/option[7]').click()     #选择龙岗区
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[6]/td[2]/input').send_keys("坂田街道")  #输入街道信息
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[8]/td[2]/input').send_keys("Jack")  #输入姓名
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[9]/td[2]/input').send_keys("123@qq.com")   #输入邮箱
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[10]/td[2]/input').send_keys("123")    #输入QQ号
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[8]/td[4]/input').send_keys("李先生")  #输入称呼
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[9]/td[4]/input').send_keys("CEO")     #输入职位
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[10]/td[4]/input').send_keys("17612345678")  #输入手机号码
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[11]/td[2]/textarea').send_keys("备注")   #输入备注
        chrome.find_element_by_xpath('//*[@id="form1"]/table/tfoot/tr/td/input[1]').click()   #点击保存
        massage = chrome.find_element_by_xpath('/html/body/div[5]/div[2]').text
        self.assertEqual("添加客户成功",massage[2:])
        now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        chrome.get_screenshot_as_file(r"D:\python_work\auto_test\img\\"+now+"customer.png")
        # chrome.find_element_by_xpath('//*[@id="form1"]/table/tfoot/tr/td/input[2]').click()   #点击保存并新建按钮
    def tearDown(self):
        chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a').click()   #点击用戶名
        chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/ul/li[12]/a').click()   #点击退出
        sleep(3)
        chrome.quit()

if __name__ == '__main__':
    unittest.main()


