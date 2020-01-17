"""配置项目路径，账号等信息"""
import os


class PathConfig:

    file_path = os.path.abspath(__file__)
    # 获取auto_test所在的路径，dirname可以获取文件夹名
    project_path = os.path.dirname(os.path.dirname(file_path))
    # 测试用例所在的路径
    testcase_path = project_path + "\\ui_test\\src\\testcase\\tools"
    report_path = project_path + "\\ui_test\\report\\"
    log_path = project_path + "\\log\\"
    excel_path = project_path + "\\excel\\"
    img_path = project_path + "\\img\\"
    data_path = project_path + "\\data\\"

if __name__ == '__main__':
    print(PathConfig.project_path)