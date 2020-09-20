# -*- coding: utf-8 -*-
# @Time : 2020/02/15
# @Author : Wind
from flask import Flask
from flask import render_template

# 1.创建Flask应用程序实例，需要传入name,作用是确定资源所在的路径
app = Flask(__name__)


# 2.定义路由及视图函数
@app.route('/', methods=['GET', 'POST'])
def index():
    # return "Hello Flask"
    url_str = "www.itheima.com"
    my_list = [1, 3, 5, 7, 9]
    my_dict = {
        'name': '黑马',
        'url': 'www.itheima.com'
    }
    # 模板中的变量名与入参变量名保持一致
    return render_template("index.html", url_str=url_str, my_list=my_list, my_dict=my_dict)


# 使用同一个视图函数来显示不同用户的订单信息
# 定义路由的参数，<>内需要起个名字
@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
    # 需要在视图函数的（）内填入参数名才能被使用
    return 'order_id: %s' % order_id


# 3.启动程序
if __name__ == '__main__':
    app.run()  # 将Flask程序在Flask提供的简易的服务器中运行（用于测试）
