import requests  #发送http请求
import json    #用来处理json数据的包

base_url = "http://192.168.0.111/wuye/public/index.php/index/index/"
p = {
    "username":15012345678,
     "password":123456,
    "token":"e10adc3949ba59abbe56e057f20f883e"
}
r = requests.get(base_url+"login?",p)    #登录
print(r)
print(r.text)     #查看返回数据中的文本(json格式)
rt = json.loads(r.text)   #将接口返回数据转换为字典
print(rt["message"])
print(r.status_code)    #查看状态码
print(r.url)    #查看请求地址

r1 = requests.get(base_url+"allCommunityId?",p)   #查询小区列表
print(r1.text)
r2 = json.loads(r1.text)   #将接口返回数据转换为字典
print(r2["message"])

q = {
    "username":15012345678,
    "token":"e10adc3949ba59abbe56e057f20f883e"
}
r3 = requests.post(base_url+"allCommunityId",q)
print(r3.text)




