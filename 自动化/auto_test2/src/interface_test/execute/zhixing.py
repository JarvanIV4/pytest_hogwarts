#测试用例的统一执行，自动添加用例的方式
import unittest
import time
import HTMLTestRunner   #生成html格式的报告的执行器
from auto_test.ui_test.src.common.auto_email import auto_email     #导入发送邮件的类
from auto_test.config import config

#定义测试套件,在定义好的路径中自动发现用例，自动添加test_开头的脚本
testcase_dir = r"D:\python_work\auto_test\interface_test\testcase\\"
suit = unittest.defaultTestLoader.discover(testcase_dir,"test_*.py")

#定义报告生成路径
report_path = r"D:\python_work\auto_test\interface_test\report\\"
#定义测试报告的文件名
now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
report_name = report_path+"AutoTest"+now+".html"
fp = open(report_name,"wb")     #以二进制写入的方式打开定义的报告

#定义可生成报告的执行器，将测试过程写入到报告中
#（测试过程写入到打开的文件中，测试人员，文档标题）
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,tester="乐科测试组",title="自动化测试报告")
runner.run(suit)
fp.close()    #关闭打开的文件
# a = auto_email()    #创建对象
# a.send_email(report_name)