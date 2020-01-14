from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()
# driver.maximize_window()
# driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_b

driver.find_element_by_id("kw").send_keys("苏宁")   #输入苏宁
sleep(1)
driver.find_element_by_id("su").click()         #点击百度一下按钮
sleep(1)
# window = driver.current_window_handle
# print(window)
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]') .click() #点击苏宁官网
# windows = driver.window_handles
# print(windows)
driver.switch_to.window(driver.window_handles[1])    #切换到第二个窗口
driver.find_element_by_xpath('//*[@id="searchKeywords"]').send_keys("小米手机")   #在苏宁搜索框中输入内容
# sleep(2)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
# sleep(2)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")
# sleep(2)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"v")
# sleep(2)
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# sleep(2)
# driver.find_element_by_id("kw").send_keys(Keys.ENTER)
# sleep(2)
# shezhi = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
# ActionChains(driver).move_to_element(shezhi).perform()     #鼠标悬停
# driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()

sleep(3)
driver.quit()
