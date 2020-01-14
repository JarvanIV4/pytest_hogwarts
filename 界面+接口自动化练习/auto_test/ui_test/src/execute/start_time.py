#设定脚本定时执行
import time
import os

start_time = input("请输入脚本开始执行的时间（例如12:00）:")
while True:
    now = time.strftime("%H:%M",time.localtime())    #获取系统时间
    if now == start_time:
        print("---开始执行脚本---")
        os.chdir(r"D:\python_work\auto_test\ui_test\src\execute\\")     #切换到总执行脚本所在的路径下
        os.system("python zhixing2.py")     #调用执行脚本
        print("\\n---脚本执行结束---")
        break
    else:
        time.sleep(10)
        print(now)