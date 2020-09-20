# -*- coding: utf-8 -*-
# @Time : 2020/6/21
# @Author : Wind
# 备份文件
from datetime import datetime
import shutil

today = datetime.today().strftime("%Y-%m-%d")
copy_dir = '/'
backup_dir = 'E:\\我的文档\\备份资料\\python源码\\' + today
shutil.copytree(copy_dir, backup_dir)
print(today + "备份成功！")