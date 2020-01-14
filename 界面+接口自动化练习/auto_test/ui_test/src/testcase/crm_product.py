#添加产品脚本、图片上传、截图、元素等待
from selenium import webdriver
import time
from time import sleep
import os
from selenium.webdriver.common.by import By   #定位方法
from selenium.webdriver.support.ui import WebDriverWait   #显式等待
from selenium.webdriver.support import  expected_conditions as ec #期望条件
import  unittest    #单元测试框架
from auto_test.data.get_data import excel_data   #封装好的Excel数据
from auto_test.data.get_name import ran_name
from auto_test.ui_test.src.common.common import method    #导入公共方法

class create_product(unittest.TestCase):
    def setUp(self):
        #用户登录
        global chrome,m
        data = excel_data()
        user = data.sheet1(1,3)    #获取第一个标签的第三行

        chrome = webdriver.Chrome()
        chrome.get("http://192.168.0.111/crm/index.php?m=user&a=login")
        m = method(chrome)
        m.login("xujianda","123456")
        # chrome.find_element_by_name("name").send_keys(user[0])
        # chrome.find_element_by_name("password").send_keys(user[1])
        # chrome.find_element_by_name("name").send_keys("xujianda")
        # chrome.find_element_by_name("password").send_keys("123456")
        # chrome.find_element_by_name("submit").click()
    def test_add_product(self):
        """测试添加产品"""
        m.click_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[1]/li[4]/a')  #点击产品
        m.click_element(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[2]/a')       #点击添加产品
        m.input_text(By.XPATH,'//*[@id="name"]',m.ran_letter())    #输入产品名称
        m.input_text(By.XPATH,'//*[@id="development_team"]',"开发团队")    #输入开发团队
        m.input_text(By.XPATH,'//*[@id="form1"]/table/tbody/tr[7]/td[2]/table/tbody/tr/td[4]/div',r"D:\html\img\222.jpg",0)
        m.click_element(By.XPATH,'//*[@id="form1"]/table/tfoot/tr/td/input[1]')
        message = chrome.find_element_by_xpath('/html/body/div[5]/div[2]').text
        print(message[2:])
        self.assertEqual("产品添加成功！",message[2:])
        # chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[4]/a').click()  #点击产品
        # chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[2]/a').click()    #点击添加产品
        # name = get_name()
        # proname = name.get_khname()
        # chrome.find_element_by_xpath('//*[@id="name"]').send_keys(proname)     #输入产品名称
        # chrome.find_element_by_xpath('//*[@id="development_team"]').send_keys("开发团队")   #输入开发团队
        # chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[7]/td[2]/table/tbody/tr/td[4]/div').click()
        # os.chdir(r"D:\python_work\autoit")     #切换到上传程序所在的文件夹
        # os.system("upload.exe")    #调用上传文件的程序
        # chrome.find_element_by_xpath('//*[@id="form1"]/table/tfoot/tr/td/input[1]').click()  #点击保存
        # message = chrome.find_element_by_xpath('/html/body/div[5]/div[2]').text
        # print(message[2:])
        # self.assertEqual("产品添加成功！",message[2:])
        # # message = chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]').text    #获取“该产品名已存在！”
        # # self.assertEqual("该产品名已存在！",message[2:])
        # now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        # chrome.get_screenshot_as_file("D:\python_work\auto_test\img\\"+now+"chanpin.png")   #截图并保存到img中

    def tearDown(self):
        #退出登录
        m.logout()

if __name__ == '__main__':
    unittest.main()


# # chrome = webdriver.Chrome()
# # chrome.get("http://192.168.0.111/crm/index.php?m=user&a=login")
# # #浏览器窗口、最长等待时间、刷新间隔
# # #期望条件中的元素被定位到，找到元素之后，会把元素对象返回给e
# # e = WebDriverWait(chrome,5,0.5).until(
# #     ec.presence_of_element_located((By.NAME,"name"))
# # )
# # e.send_keys("admin")
# # chrome.implicitly_wait(10)    #隐式等待
# # # chrome.find_element_by_name("name").send_keys("xujianda")
# # chrome.find_element_by_name("password").send_keys("123456")
# # chrome.find_element_by_name("submit").click()
# chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[4]/a').click()  #点击产品
# chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[2]/a').click()    #点击添加产品
# chrome.find_element_by_xpath('//*[@id="name"]').send_keys("产品名称45654")     #输入产品名称
# # frame = chrome.find_element_by_xpath('/html/body/div[7]/iframe')
# # chrome.switch_to.frame(frame)
# # chrome.find_element_by_xpath('//*[@id="development_time"]').send_keys("2019-01-18")
# # chrome.find_element_by_xpath('//*[@id="dpOkInput"]').click()
# # chrome.switch_to.default_content()
# chrome.find_element_by_xpath('//*[@id="development_team"]').send_keys("开发团队")   #输入开发团队
# #方法1：使用send_keys()方法实现文件上传
# # chrome.find_element_by_xpath('//*[@id="main_pic"]').send_keys(r"D:\html\img\222.jpg")
# #方法2：
# chrome.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[7]/td[2]/table/tbody/tr/td[4]/div').click()
# os.chdir(r"D:\python_work\autoit")     #切换到上传程序所在的文件夹
# os.system("upload.exe")    #调用上传文件的程序
# chrome.find_element_by_xpath('//*[@id="form1"]/table/tfoot/tr/td/input[1]').click()  #点击保存
# # chrome.find_element_by_xpath('//*[@id="form1"]/table/tfoot/tr/td/input[2]').click()  #点击保存并新建
# #时间戳
# now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
# chrome.get_screenshot_as_file("D:\python_work\auto_test\img\\"+now+"chanpin.png")   #截图并保存到img中
#
# chrome.quit()

