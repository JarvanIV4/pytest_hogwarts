# -*- coding: utf-8 -*-
# @Time : 2020/02/29
# @Author : Wind

from python框架.flask_test.flask_demo.flask_SQLalchemy_demo import *
u = User()
print(u.query.all())
print(u.query.count())
print(u.query.first())
print(u.query.get(1))
print(u.query.filter_by(id=1).first())
print(u.query.filter(User.id==1).first())