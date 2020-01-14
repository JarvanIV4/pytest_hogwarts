import unittest
from auto_test.interface_test.interface.interface import inter

class login(unittest.TestCase):
    def setUp(self):
        global a
        a = inter()

    def test_login_1(self):
        """登录接口_正例"""
        rt =  a.login("15012345678","123456")
        self.assertEqual("success",rt["message"])

    def test_login_2(self):
        """登录接口_密码错误"""
        rt = a.login("15012345678","123")
        self.assertEqual("user is error",rt["message"])

    def tearDown(self):
        print("登录接口测试结束")

if __name__ == '__main__':
    unittest.main()