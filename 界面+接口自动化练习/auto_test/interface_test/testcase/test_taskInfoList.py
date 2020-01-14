import unittest   #导入单元测试框架
from auto_test.interface_test.interface.interface import inter

class Community(unittest.TestCase):
     def setUp(self):
         global a
         print("开始测试小区列表接口")
         a = inter()

     def test_userinfo_1(self):
         """用户信息接口_正例"""
         rt = a.userinfo("15012345678")
         self.assertEqual("success",rt["message"])    #使用断言判断接口返回数据是否符合预期

     def test_userinfo_2(self):
         """用户信息接口_用户名不存在"""
         rt = a.userinfo("15012312312")
         self.assertEqual("user is error",rt["message"])

     def tearDown(self):
         print("用户信息接口结束")

if __name__ == '__main__':
    unittest.main()