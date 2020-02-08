"""封装用例脚本中的操作方法"""
from selenium.webdriver.support.ui import WebDriverWait    #显示等待
from selenium.webdriver.support import expected_conditions as ec    #期望条件
from selenium.webdriver.common.by import By
from random import Random
from auto_test.ui_test.src.common.log import log
from time import sleep

class method():

    def __init__(self,browser):
        self.driver = browser    #类中的初始化方法，需要在创建对象时赋值
        self.log = log("auto_test.log")     #创建对象，并配置日志文件名

    def login(self,username,password):
        #登录CRM系统
        self.input_text(By.NAME,"name",username)
        self.input_text(By.NAME,"password",password)
        self.click_element(By.NAME,"submit")

    def logout(self):
        #退出CRM系统
        self.click_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a")
        self.click_element(By.LINK_TEXT,"退出")
        self.driver.quit()

    def login_oa(self,username,password):
        #登录OA系统
        self.input_text(By.ID,"account",username)
        self.input_text(By.ID,"password",password)
        self.click_element(By.ID,"submit")

    def logout_oa(self):
        #退出OA系统
        # self.click_element(By.XPATH,'//*[@id="start"]')
        # self.click_element(By.XPATH,'//*[@id="startMenu"]/li[10]/a')
        self.click_element(By.XPATH,'//*[@id="bottomRightBar"]/ul/li[1]')
        self.driver.quit()


    def locate_element(self,*loc):
        """封装定位元素的方法：采用显示等待来定位元素
        *loc代表可以传入多个参数，并把传入的参数保存为元组，例如传入loc1，loc2
        loc1:采用的定位方式，例如By.NAME
        loc2:定位方式对应的值，例如："name"
        """
        try:
            #(1.浏览器对象 2.最长等待时间 3.刷新间隔)
            element = WebDriverWait(self.driver,5,0.5).until(
                #期望条件是：直到元素被定位到
                ec.presence_of_element_located((loc))
            )
            return element
        except:
            self.log.error("元素定位失败"+str(loc))     #打印报错信息

    def input_text(self,loc1,loc2,value,clear=True):
        """封装输入文本的方法
        loc1:采用的定位方式，例如By.NAME
        loc2:定位方式对应的值，例如："name"
        value:需要输入的文本
        """
        if clear:
            try:
                self.locate_element(loc1,loc2).clear()
                self.locate_element(loc1,loc2).send_keys(value)
                self.log.error("输入文本"+str(value))
            except:
                self.log.error("输入文本失败"+str(value))
        else:
            try:
                self.locate_element(loc1,loc2).send_keys(value)
                self.log.error("输入文本"+str(value))
            except:
                self.log.error("输入文本失败"+str(value))

    def click_element(self,loc1,loc2):
        """封装点击的方法"""
        try:
            self.locate_element(loc1,loc2).click()
            self.log.info("点击元素"+str(loc1)+str(loc2))
        except:
            self.log.info("点击元素失败"+str(loc1)+str(loc2))

    def ran_name(self):
        """产生随机名字"""
        ran = Random()
        name = ""
        str1 = "科成功和兴"
        name = "赵"
        for j in range(2):
            m = ran.randrange(len(str1)-1)
            name = name + str1[m]
        return name

    def ran_letter(self):
        #产生随机英文名字
        ran = Random()
        base = "abcdefghijklmnopqrstuvwxyz1234567890"
        name = ""
        for j in range(ran.randint(5,10)):
            m = ran.randrange(len(base)-1)
            name = name + base[m]
        return name