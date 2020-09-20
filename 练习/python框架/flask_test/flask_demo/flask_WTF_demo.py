# -*- coding: utf-8 -*-
# @Time : 2020/02/15
# @Author : Wind
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

# 1.创建Flask应用程序实例，需要传入name,作用是确定资源所在的路径
app = Flask(__name__)
app.secret_key = 'itheima'  # flash需要设置secret_key对消息加密


class Login(FlaskForm):
    username = StringField("用户名:", validators=[DataRequired()])
    password = PasswordField("密码:", validators=[DataRequired()])
    password2 = PasswordField("确认密码:", validators=[DataRequired(), EqualTo(password, "两次密码输入不一致")])
    submit = SubmitField("提交")


@app.route('/', methods=['GET', 'POST'])
def login():
    login_form = Login()
    # 获取请求参数
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    # 判断请求方式
    if request.method == 'POST':
        # 验证参数
        if login_form.validate_on_submit():
            print(username, password, password2)
            return "success"
        else:
            flash("参数有误")
    return render_template("index2.html", login_form=login_form)


# 2.定义路由及视图函数
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print(username, password, password2)
        if not all([username, password, password2]):
            print("参数不完整")
            flash("参数不完整")
        elif password != password2:
            print("密码不一致, %s!=%s" % (password, password2))
            flash("密码不一致")
        else:
            return 'success'
    return render_template("index2.html")


# 3.启动程序
if __name__ == '__main__':
    app.run()  # 将Flask程序在Flask提供的简易的服务器中运行（用于测试）
