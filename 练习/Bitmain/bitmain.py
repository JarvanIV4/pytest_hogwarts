from selenium import webdriver
from time import sleep


class Bitmain():

    def __init__(self):
        self.url = "https://account.bitmain.com/sign_in?method=2&service=https%3A%2F%2Fservice.bitmain.com.cn" \
                   "%2Fwetseasonfestival "
        self.driver = webdriver.Chrome()

    def login(self, username, password):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/div/div[1]/div[2]/form/div['
                                          '1]/div/div/span/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/div/div[1]/div[2]/form/div['
                                          '2]/div/div/span[1]/input').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/div/div[1]/div[2]/form/div['
                                          '3]/button').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/section[1]/div/div[1]/button').click()
        sleep(5)


if __name__ == '__main__':
    t = Bitmain()
    t.login("2268035948@qq.com", "123456-abc")
