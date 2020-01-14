"""
操作文本文档
"""
fp = open("user.txt")
# content = fp.read()
# print(content)
#以行的方式读取文档内容，并保存为列表格式
content1 = fp.readlines()
print(content1)
# print(content1[2])
fp.close()

with open("user1.txt","w") as fp:
    fp.writelines("PyCharm\n")
    fp.writelines("PyCharm")

with open("cfb.txt","w") as fp:
    for i in range(1,10):
        for j in range(1,i+1):
           fp.writelines("%d×%d=%d "%(j,i,i*j))
        fp.writelines("\n")

from auto_test.data.get_data import excel_data
e = excel_data()
li = e.sheet1(1)
print(li)