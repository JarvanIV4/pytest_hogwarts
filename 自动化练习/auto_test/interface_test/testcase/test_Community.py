import unittest   #导入单元测试框架
from auto_test.interface_test.interface.interface import inter

class Community(unittest.TestCase):
     def setUp(self):
         global a
         print("开始测试小区列表接口")
         a = inter()

     def test_Community_1(self):
         """获取小区列表接口_正例"""
         re = a.login("15012345678","123456")
         token = re["content"]["token"]
         rt = a.allCommunityId("15012345678",token)
         self.assertEqual("success",rt["message"])    #使用断言判断接口返回数据是否符合预期

     def test_Community_2(self):
         """测试小区列表接口_token失效"""
         rt = a.allCommunityId("15012345678","abc")
         self.assertEqual("token failed",rt["message"])

     def test_Community_3(self):
         """测试小区列表接口_用户名不存在"""
         rt = a.allCommunityId("15012312312","abc")
         self.assertEqual("user is error",rt["message"])

     def tearDown(self):
         print("测试小区列表接口结束")

if __name__ == '__main__':
    unittest.main()