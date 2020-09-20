# -*- coding: utf-8 -*-
# @Time : 2020/02/16
# @Author : Wind
from 练习.python框架.flask_test.flask_demo.flask_SQLalchemy_demo import *

db.drop_all()  # 删除表
db.create_all()  # 创建表
# 新增数据
role = Role(name='admin')
db.session.add(role)
db.session.commit()

user = User(name='heima', role_id=role.id)
db.session.add(user)
db.session.commit()

# 修改数据
user.name = 'chengxuyuan'
db.session.commit()


# 删除数据
db.session.delete(user)
db.session.commit()
