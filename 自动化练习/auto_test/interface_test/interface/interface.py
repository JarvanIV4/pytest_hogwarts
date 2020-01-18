import requests
import json

class inter():

    def __init__(self):
        self.base_url = "http://192.168.0.111/wuye/public/index.php/index/index/"

    def login(self,username,password):
        """封装登录接口"""
        try:
            path = "login?"
            p = {
                "username":username,
                "password":password
            }
            r = requests.get(self.base_url+path,p)   #使用get方法
            rt = json.loads(r.text)           #将json格式的数据转换为字典型
            return rt
        except:
            return "登录接口访问失败"

    def userinfo(self,username):
        """账号信息接口"""
        try:
            path = "oauthAccount?"
            p = {
                "username":username
            }
            r = requests.get(self.base_url+path,p)   #使用get方法
            rt = json.loads(r.text)           #将json格式的数据转换为字典型
            return rt
        except:
            return "登录接口访问失败"


    def allCommunityId(self,username,token):
        """查询小区列表接口"""
        try:
            path = "allCommunityId?"
            p = {
                "username":username,
                "token":token
            }
            r = requests.get(self.base_url+path,p)
            rt = json.loads(r.text)
            return rt
        except:
            return "小区列表接口访问失败"

    def buildingInfoList(self,username,token):
        """查询楼栋列表接口"""
        try:
            path = "buildingInfoList?"
            p = {
                "username":username,
                "token":token,
                "communityId":1
            }
            r = requests.get(self.base_url+path,p)
            rt = json.loads(r.text)
            return rt
        except:
            return "楼栋列表接口访问失败"

    def taskInfo(self,username,token):
        """添加工单接口"""
        try:
            path = "taskInfo?"
            p = {
                "createorName":"abc",
                "residentName":"abc",
                "username":username,
                "token":token,
                "telephone":15012345678,
                "houseId":1,
                "content":"添加工单"
            }
            r = requests.get(self.base_url+path,p)
            rt = json.loads(r.text)
            return rt
        except:
            return "添加工单接口访问失败"


if __name__ == '__main__':
    a =  inter()
    re = a.login("15012345678","123456")
    print(re)
    token = re["content"]["token"]
    print(token)
    r2 = a.allCommunityId(15012345678,token)
    print(r2)
    r3 = a.buildingInfoList(15012345678,token)
    print(r3)
    r4  = a.taskInfo(15012345678,token)
    print(r4)
    r5 = a.userinfo("15012345678")
    print(r5)
