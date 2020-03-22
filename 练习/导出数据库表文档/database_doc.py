# -*- coding: utf-8 -*-
# @Time : 2020/03/19
# @Author : Wind
import pymysql
import xlwt


class DatebaseDoc:

    def query_info(self):
        db = MysqlTools()
        db.connect_mysql('111.230.139.146', 'bxqqedu', '69eFFF11@b4f4-11e9#a294*0235d2b38928', 'bxqqedu')
        db.write_to_excel('s', 'bxqqedu', 't_sc_user')
        # result = db.query_info('bxqqedu', 't_sc_user')



class MysqlTools:

    def connect_mysql(self, host, user, passwd, db=None):
        """
        连接Mysql数据库
        :param host: 主机IP地址
        :param user: 用户名
        :param passwd: 密码
        :param db: 数据库
        """
        # 连接数据库
        self.connect = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=db, charset='utf8')
        if self.connect.open:
            print("连接数据库{0}成功".format(db))
        else:
            print("连接数据库{0}失败".format(db))
        self.cursor = self.connect.cursor()  # 使用cursor方法创建一个游标
        return self.connect, self.cursor

    def execute_the_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except:
            self.connect.rollback()

    def disconnect_to_db(self):
        """
        断开数据库连接
        """
        self.cursor.close()
        self.connect.close()
        if self.connect.open is False:
            print("已断开数据库连接")

    def query_sql(self, sql, return_type='tuple'):
        """
        查询数据库
        :param sql: 查询SQL语句
        :param return_type: 返回类型-元组('tuple')或字典('dict')
        :return: result: 查询结果
        """
        try:
            self.cursor.execute(sql)
            if return_type == 'tuple':
                result = self.cursor.fetchall()
                return result
            if return_type == 'dict':  # 将查询结果转换为字典
                columns = [desc[0] for desc in self.cursor.description]
                result = [dict(zip(columns, row)) for row in self.cursor]
                return result
        except:
            self.connect.rollback()

    def query_count(self, sql):
        self.cursor.execute(sql)
        return self.cursor.rowcount

    def query_info(self, table_schema, table_name):
        sql = "SELECT (@rowNum:=@rowNum+1) as 序号,COLUMN_NAME 列名,COLUMN_TYPE 数据类型,DATA_TYPE 字段类型," \
              "CHARACTER_MAXIMUM_LENGTH 长度,IS_NULLABLE 是否为空,COLUMN_DEFAULT 默认值,COLUMN_COMMENT 备注 " \
              "FROM INFORMATION_SCHEMA.COLUMNS,(SELECT @rownum:=0) r " \
              "WHERE table_schema='{0}' AND table_name='{1}'".format(table_schema, table_name)
        print(sql)
        db_desc_result = self.query_sql(sql)
        print(db_desc_result)
        print(self.query_count(sql))
        return db_desc_result

    def write_to_excel(self, excel_name, table_schema, table_name):
        font_style = xlwt.XFStyle()  # 二进制
        font_style.font.bold = True  # 表头内容
        desc = self.query_info(table_schema, table_name)

        columns = ["序号", "列名", "数据类型", "字段类型", "长度", "是否为空", "默认值", "备注"]  # 表头字段
        wbk = xlwt.Workbook()  # 实例化一个Excel
        sheet1 = wbk.add_sheet('sheet1')  # 添加该Excel的第一个sheet，cell_overwrite_ok=True
        row_num = 3
        # 写入字段名
        for col_num in range(len(columns)):
            sheet1.write(row_num, col_num, columns[col_num], font_style)
        # 写入字段属性
        for row in range(len(desc)):
            for col in range(len(columns)):
                sheet1.write(row+row_num+1, col, desc[row][col], font_style)
        filename = excel_name + '.xls'  # 定义Excel名字
        wbk.save(filename)  # 保存Excel


if __name__ == '__main__':
    # t = MysqlTools()
    # t.write_to_excel('s', 'bxqqedu', 't_sc_user')
    t = DatebaseDoc()
    t.query_info()
