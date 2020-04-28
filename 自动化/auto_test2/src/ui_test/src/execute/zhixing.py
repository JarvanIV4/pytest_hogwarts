#执行脚本，用来调用测试用例的执行
import unittest
from auto_test.ui_test.src.testcase.crm_product import create_product
from auto_test.ui_test.src.testcase.crm_test_leads import create_leads
from auto_test.ui_test.src.testcase.crm_test_customer import create_customer

#第一种统一执行测试的方式（手动添加用例）
suit = unittest.TestSuite()    #定义测试套件
#添加测试用例，需要直接添加到test_方法
suit.addTest(create_product("test_add_product"))
suit.addTest(create_leads("test_add_leads"))
suit.addTest(create_customer("test_add_customer"))

#定义执行器，用来执行测试套件
runner = unittest.TextTestRunner()
runner.run(suit)    #执行定义好的套件