from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 配置数据库的地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flask_sql_demo'
# 跟踪数据库的修改，不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 数据库模型
class Role(db.Model):
    __tablename__ = 'roles'  # 定义表名
    # 定义字段,db.Column表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # 在一的一方写关联,表示和User模型发生了关联，增加了一个users属性
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role: %s %s>' % (self.name, self.id)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # db.ForeignKey表示外键 表名.字段名
    # user希望有role属性，但这个属性的定义需要在另一个模型中定义
    def __repr__(self):
        return '<User: %s %s %s %s>' % (self.id, self.name, self.email, self.password)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    db.drop_all()   # 删除表
    db.create_all() # 创建表
