#申请调休
from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
chrome.get("http://192.168.0.110/ranzhi/www/sys/user-login")
chrome.find_element_by_xpath('//*[@id="account"]').send_keys("xujianda")
chrome.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
chrome.find_element_by_xpath('//*[@id="submit"]').click()
sleep(1)
chrome.find_element_by_xpath('//*[@id="s-menu-2"]/button').click()    #点击日常办公
chrome.switch_to.frame("iframe-2")     #切换到iframe-2中
chrome.find_element_by_xpath('//*[@id="mainNavbar"]/ul/li[8]/a').click()  #点击调休
chrome.find_element_by_xpath('//*[@id="menuActions"]/a').click()      #点击申请调休
sleep(1)
chrome.find_element_by_xpath('//*[@id="begin"]').send_keys('2019-01-28')   #输入开始日期
chrome.find_element_by_xpath('//*[@id="start"]').clear()      #清空默认开始时间
chrome.find_element_by_xpath('//*[@id="start"]').send_keys('10:20')      #输入开始时间
chrome.find_element_by_xpath('//*[@id="end"]').send_keys('2019-01-29')    #输入结束日期
chrome.find_element_by_xpath('//*[@id="finish"]').clear()         #清空默认结束时间
chrome.find_element_by_xpath('//*[@id="finish"]').send_keys('18:10')     #输入结束时间
chrome.find_element_by_xpath('//*[@id="overtime_chosen"]/ul').click()   #点击加班记录
chrome.find_element_by_xpath('//*[@id="overtime_chosen"]/div/ul/li').click()     #选择加班记录
chrome.find_element_by_xpath('//*[@id="desc"]').send_keys("事由")      #输入事由
chrome.find_element_by_xpath('//*[@id="submit"]').click()      #点击确定

sleep(5)
chrome.quit()