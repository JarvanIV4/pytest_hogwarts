# -*- coding: utf-8 -*-
# @Time : 2020/02/29
# @Author : Wind

from python框架.flask_test.flask_demo.flask_SQLalchemy_demo import *

role = Role(name='admin')
db.session.add(role)
db.session.commit()
user1 = User(name='张三', role_id=role.id)
user2 = User(name='李四', role_id=role.id)
db.session.add_all([user1, user2])
db.session.commit()
