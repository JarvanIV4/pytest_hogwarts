from selenium import webdriver
import time
from time import sleep


class Bitmain():

    def bitmain_main(self):
        """
        用户在17：55~17: 58随机登录，然后等到18:00:00准时点击‘领取购物券’按钮
        """
        # TODO 用户在17：55~17: 58随机登录

    def __init__(self):
        self.login_url = "https://account.bitmain.com/sign_in?method=2&service=https%3A%2F%2Fservice.bitmain.com.cn%2Fwetseasonfestival"
        self.click_time = "17:59:58"
        list(self.click_time)[5] = 1
        self.end_time = ''.join([str(i) for i in self.click_time])

    def login(self, username, password):
        self.driver = webdriver.Chrome()
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
        while True:
            now = time.strftime("%H:%M:%S", time.localtime())  # 获取系统时间
            if now == self.click_time:
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/section[1]/div/div[1]/button').click()  # 点击“领取购物券”
                print("点击成功")
            elif now == self.end_time:
                break
            else:
                sleep(1)
                print(now)

    def start_job(self, login_time, username, password):
        """
        定时任务
        :param login_time: 登录时间
        :param username: 用户名
        :param password: 密码
        """
        while True:
            now = time.strftime("%H:%M", time.localtime())  # 获取系统时间
            if now == login_time:
                print("---登录Bitmain---")
                self.login(username, password)
                break
            else:
                time.sleep(10)
                print(now)


if __name__ == '__main__':
    username = '2268035948@qq.com'
    password = '123456-abc'
    t = Bitmain()
    t.start_job("11:58", username, password)