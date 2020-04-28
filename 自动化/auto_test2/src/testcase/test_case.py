import unittest

class test_case(unittest.TestCase):
    def setUp(self):
        print("测试开始")
    def test_add(self):
        a = 100
        b = 100
        self.assertEqual(300,a+b,msg="测试不通过")
    def tearDown(self):
        print("测试结束")

if __name__ == '__main__':
    unittest.main()