from selenium import webdriver
import time
import os
from time import sleep


class Bitmain():

    def bitmain_main(self):
        """
        用户在17：55~17: 58随机登录，然后等到18:00:00准时点击‘领取购物券’按钮
        """
        # TODO 用户在17：55~17: 58随机登录

    def __init__(self):
        self.login_url = "https://account.bitmain.com/sign_in?method=2"
        self.driver = webdriver.Chrome()

    def login(self, username, password):
        self.driver.get(self.login_url)     # 打开登录网址
        self.driver.maximize_window()       # 最大化窗口
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/div/div[1]/div[2]/form/div['
                                          '1]/div/div/span/input').send_keys(username)  # 输入用户名
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/div/div[1]/div[2]/form/div['
                                          '2]/div/div/span[1]/input').send_keys(password)  # 输入密码
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/div/div[1]/div[2]/form/div['
                                          '3]/button').click()  # 点击登录
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/section[1]/div/div[1]/button').click()  # 点击“领取购物券”
        sleep(5)

    def start_job(self, start_time):
        """
        定时任务
        :param start_time: 定时任务的启动时间
        """
        while True:
            now = time.strftime("%H:%M", time.localtime())  # 获取系统时间
            if now == start_time:
                print("---登录Bitmain---")
                os.chdir(r"D:\python_work\auto_test\ui_test\src\execute\\")  # 切换到总执行脚本所在的路径下
                os.system("python zhixing2.py")  # 调用执行脚本
                break
            else:
                time.sleep(10)
                # print(now)


if __name__ == '__main__':
    t = Bitmain()
    t.login("2268035948@qq.com", "123456-abc")
