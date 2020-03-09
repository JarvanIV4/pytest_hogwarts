# -*- coding: utf-8 -*-
# @Time : 2020/02/16
# @Author : Wind
from python框架.flask_test.flask_demo.flask_SQLalchemy_demo import *

class FlaskSQL:

    def __init__(self):
        db.drop_all()  # 删除表
        db.create_all()  # 创建表
        global role, user
        role = Role(name='admin')
        db.session.add(role)
        db.session.commit()

        user = User(name='heima', role_id=role.id)
        db.session.add(user)
        db.session.commit()

    def add(self):
        # 新增数据
        pass
        # role = Role(name='admin')
        # db.session.add(role)
        # db.session.commit()
        #
        # user = User(name='heima', role_id=role.id)
        # db.session.add(user)
        # db.session.commit()

    def update(self):
        # 修改数据
        user.name = 'chengxuyuan'
        db.session.commit()

    def delete(self):
        # 删除数据
        db.session.delete(user)
        db.session.commit()

if __name__ == '__main__':
    flask = FlaskSQL()
    # flask.add()
    flask.update()
    # flask.delete()