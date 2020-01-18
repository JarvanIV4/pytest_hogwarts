"""配置项目路径，账号等信息"""
import os

#当前文件的路径  __file__是每个脚本自带的变量 相当于路径+文件名
#abspath   可以将__file__转换为正常的路径格式
file_path = os.path.abspath(__file__)
# 获取auto_test所在的路径，dirname可以获取文件夹名
project_path = os.path.dirname(os.path.dirname(file_path))
# 测试用例所在的路径
testcase_path = project_path+"\\ui_test\\src\\testcase\\tools"
report_path = project_path+"\\ui_test\\report\\"

log_path = project_path+"\\ui_test\\log\\"
excel_path = project_path+"\\excel\\"
img_path = project_path+"\\img\\"
data_path = project_path+"\\data\\"