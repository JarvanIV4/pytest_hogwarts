# -*- coding: utf-8 -*-
# @Time : 2020/03/19
# @Author : Wind
import pymysql
import xlwt


class DatebaseDoc:

    def query_info(self):
        db = MysqlTools()
        db.connect_mysql('111.230.139.146', 'bxqqedu', '69eFFF11@b4f4-11e9#a294*0235d2b38928', 'bxqqedu')
        sql = "select * from t_sc_user where id=1"
        result = db.query_sql(sql)
        print(result)


class MysqlTools:

    def connect_mysql(self, host, user, passwd, db=None):
        """
        连接Mysql数据库
        :param host: 主机IP地址
        :param user: 用户名
        :param passwd: 密码
        :param db: 数据库
        """
        # 打开数据库连接
        self.database = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=db, charset='utf8')
        return self.database

    def execute_the_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.database.commit()
        except:
            self.database.rollback()

    def disconnect_to_db(self):
        self.cursor.close()
        self.database.close()

    def query_sql(self, sql, return_type='tuple'):
        """
        查询数据库
        :param sql: 查询SQL语句
        :param return_type: 返回类型-元组('tuple')或字典('dict')
        :return: result: 查询结果
        """
        try:
            self.cursor = self.database.cursor()  # 使用cursor方法创建一个游标
            cursor = self.cursor.execute(sql)
            if return_type == 'tuple':
                result = self.cursor.fetchall()
                return result
            if return_type == 'dict':  # 将查询结果转换为字段
                columns = [i[0] for i in cursor.description]
                result = [dict(zip(columns, row)) for row in cursor]
                return result
        except:
            self.database.rollback()

    def query_info(self, sql):
        sql = ""
        result = self.query_sql(sql)
        print(result)
        return result

    def write_to_excel(self, name):
        font_style = xlwt.XFStyle()  # 二进制
        font_style.font.bold = True  # 表头内容
        columns = ['单位名称', '纳税人识别号', '个税申报密码', '申报结果', '错误原因', '是否确认申报']  # 写进表头内容
        wbk = xlwt.Workbook()  # 实例化一个Excel
        sheet1 = wbk.add_sheet('sheet1', cell_overwrite_ok=True)  # 添加该Excel的第一个sheet
        row_num = 0
        for col_num in range(len(columns)):
            sheet1.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()  # 将列名加粗后重新设置

        # fileds = ['ID编号', '名字']  # 直接定义结果集的各字段名
        # wbk = xlwt.Workbook()  # 实例化一个Excel
        #
        # for filed in range(0, len(fileds)):  # 写入字段信息
        #     sheet1.write(0, filed, fileds[filed][0])
        # for row in range(1, len(result) + 1): # 写入SQL查询数据
        #     for col in range(0, len(fileds)):
        #         sheet1.write(row, col, result[row - 1][col])
        filename = name + '.xls'  # 定义Excel名字
        wbk.save(filename)  # 保存Excel

    # def wite_to_excel(name):
    #     filename = name + '.xls'  # 定义Excel名字
    #     wbk = xlwt.Workbook()  # 实例化一个Excel
    # 　　sheet1 = wbk.add_sheet('sheet1', cell_overwrite_ok=True)  # 添加该Excel的第一个sheet，如有需要可依次添加sheet2等
    # 　　fileds = [u'ID编号', u'名字']  # 直接定义结果集的各字段名
    # 　　execude_sql(1024)  # 调用函数执行SQL，获取结果集
    # 　　for filed in range(0, len(fileds)):  # 写入字段信息
    #         sheet1.write(0, filed, fileds[i])
    # 　　for row in range(1, len(result) + 1): 　　  # 写入SQL查询数据
    # 　　　　for col in range(0, len(fileds))
    #     　　　　　　sheet1.write(row, col, result[row - 1][col])
    # 　　wbk.save(filename)　　  # 保存Excel

if __name__ == '__main__':
    # t = MysqlTools()
    # t.write_to_excel('s')
    t = DatebaseDoc()
    t.query_info()
