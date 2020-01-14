import unittest
from auto_test.interface_test.interface.interface import inter

class buildingInfoList(unittest.TestCase):
    def setUp(self):
        global a,token
        a = inter()
        re = a.login("15012345678","123456")
        token = re["content"]["token"]

    def test_buildingInfoList_1(self):
        """楼栋信息接口_正例"""
        rt = a.buildingInfoList("15012345678",token)
        self.assertEqual("success",rt["message"])

    def test_buildingInfoList_2(self):
        """楼栋信息接口_用户名不存在"""
        re = a.buildingInfoList("15011111111",token)
        self.assertEqual("user is error",re["message"])

    def tearDown(self):
        print("楼栋信息接口测试结束")

if __name__ == '__main__':
    unittest.main()




