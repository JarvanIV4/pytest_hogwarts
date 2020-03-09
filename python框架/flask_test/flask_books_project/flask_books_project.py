from flask import Flask, render_template, flash,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
'''
1.配置数据库
2.配置模型
3.添加数据
4.使用模型显示数据库查询的数据
5.使用WTF显示表单
6.实现相关的增删改
'''

# 1.配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flask_books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # 关闭自动跟踪修改
app.secret_key = '123456'
db = SQLAlchemy(app)    # 创建数据库对象

# 定义作者模型
class Author(db.Model):
    # 表名
    __tablename__ = 'authors'
    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 关系引用
    books = db.relationship('Book', backref='author')
    def __repr__(self):
        return '<Author: %s %s>' % (self.name, self.id)


class Book(db.Model):
    # 表名
    __tablename__ = 'books'
    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    def __repr__(self):
        return '<Book: %s %s>' % (self.name, self.id)

# 自定义表单类
class AuthorForm(FlaskForm):
    author = StringField('作者', validators=[DataRequired()])
    book = StringField('作者', validators=[DataRequired()])
    submit = SubmitField('提交')


@app.route('/', methods=['GET', 'POST'])
def index():
    authors = Author.query.all()
    author_form = AuthorForm()
    '''
    验证逻辑
    1.调用WTF的函数实现验证
    2.验证通过获取数据
    3.判断作者是否存在
    4.如果作者存在，判断书籍是否存在，没有重复书籍就添加数据，如果重复就提示错误
    5.如果作者不存在，添加作者和书籍
    6.验证不通过就提示错误
    '''
    # 1.调用WTF的函数实现验证
    if author_form.validate_on_submit():
        # 2.验证通过获取数据
        author_name = author_form.author.data
        book_name = author_form.book.data
        # 3.判断作者是否存在
        author = Author.query.filter.by(name=author_name).first()
        # 4.如果作者存在.
        if author:
            pass
        else:
            # 5.如果作者不存在，添加作者和书籍
            pass
    else:
    # 5.验证不通过就提示错误
        if request.method == 'POST':
            flash('参数不全')

    return render_template('books.html', authors=authors, form=author_form)


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # # 作者表数据
    # au1 = Author(name='老王')
    # au2 = Author(name='老李')
    # au3 = Author(name='老刘')
    # db.session.add_all([au1, au2, au3])
    # db.session.commit()
    # # 书籍表数据
    # bk1 = Book(name='老王回忆录', author_id=au1.id)
    # bk2 = Book(name='历史', author_id=au1.id)
    # bk3 = Book(name='数学', author_id=au2.id)
    # bk4 = Book(name='语文', author_id=au3.id)
    # bk5 = Book(name='地理', author_id=au3.id)
    # db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # db.session.commit()
    app.run(debug=True)
