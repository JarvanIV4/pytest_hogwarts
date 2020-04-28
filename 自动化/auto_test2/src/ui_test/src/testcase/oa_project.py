from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
chrome.get("http://192.168.0.110/ranzhi/www/sys/user-login")
chrome.find_element_by_xpath('//*[@id="account"]').send_keys("xujianda")
chrome.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
chrome.find_element_by_xpath('//*[@id="submit"]').click()
sleep(2)
# chrome.find_element_by_xpath('//*[@id="mainNavbar"]/div/ul[2]/li[3]/a').click()
chrome.find_element_by_css_selector('ul.nav:nth-child(2) > li:nth-child(3) > a:nth-child(1)').click()   #点击项目
#当iframe标签有name时，可以直接使用name属性进行切换
#如果没有name属性，还可以通过xpth属性来定位到iframe，再进行切换
chrome.switch_to.frame("iframe-dashboard")    #切换进入
# frame = chrome.find_element_by_xpath('//*[@id="iframe-dashboard"]')
# chrome.switch_to.frame(frame)
chrome.find_element_by_xpath('/html/body/div/div/table/thead/tr/th[9]/a').click()  #点击创建项目
chrome.switch_to.default_content()   #切换回原页面
chrome.switch_to.frame("iframe-3")   #切换进入创建项目页面
chrome.find_element_by_xpath('//*[@id="name"]').send_keys("Project")    #输入项目名
chrome.find_element_by_xpath('//*[@id="manager_chosen"]/a/span').click()    #点击负责人
chrome.find_element_by_xpath('//*[@id="manager_chosen"]/div/ul/li[52]').click()   #选择负责人
#方法2.调用js语句修改元素的属性
#定义js，通过id找到指定元素，并修改元素的显示属性为block
# js = 'var a=document.getElementById("manager").style.display="block"'
# chrome.execute_script(js)
# chrome.find_element_by_xpath('//*[@id="manager"]/option[4]').click()
chrome.find_element_by_xpath('//*[@id="begin"]').click()        #点击开始时间
chrome.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr[3]/td[5]').click()  #选择开始时间
chrome.find_element_by_xpath('//*[@id="end"]').click()    #点击结束时间
chrome.find_element_by_xpath('/html/body/div[4]/div[3]/table/tbody/tr[5]/td[4]').click()     #选择结束时间
# chrome.switch_to.frame('')
chrome.find_element_by_xpath('//*[@id="whitelist1"]').click()
chrome.find_element_by_xpath('//*[@id="submit"]').click()    #点击保存
chrome.switch_to.default_content()    #切换为原网页
chrome.find_element_by_xpath('//*[@id="start"]').click()   #点击左下角头像
chrome.find_element_by_xpath('//*[@id="startMenu"]/li[10]/a').click()   #点击退出


sleep(3)
# chrome.quit()