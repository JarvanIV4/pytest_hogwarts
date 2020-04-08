# -*- coding: utf-8 -*-
# @Time : 2020/03/19
# @Author : Wind
import pymysql
import xlwt


class DatebaseXls:

    def dbx_main(self, excel_name, db_name='bxqqedu'):
        db = MysqlTools()
        db.connect_mysql('111.230.139.146', 'bxqqedu', '69eFFF11@b4f4-11e9#a294*0235d2b38928', db_name)
        tables = db.query_table_name(db_name)
        self.db_to_excel(excel_name, db_name, ['t_sc_online_course'])


    def db_to_excel(self, excel_name, db_name, tables):
        """
        查询数据库信息生成Excel
        :param excel_name: Excel表名称
        :param db_name: 数据库名称
        :param tables: 需要生成的数据库表名（列表）
        """
        db = MysqlTools()
        db.connect_mysql('111.230.139.146', 'bxqqedu', '69eFFF11@b4f4-11e9#a294*0235d2b38928', db_name)
        wbk = xlwt.Workbook()  # 实例化一个Excel
        tables_comment = []  # 全部表名
        i = 0
        for table_name in tables:
            desc = db.query_table_info(db_name, table_name)     # 查询数据库表名
            columns = ["序号", "列名", "数据类型", "字段类型", "长度", "是否为空", "默认值", "备注"]  # 表头字段
            sql = "select table_name 表名,table_comment 注释 from information_schema.tables " \
                  "where table_schema='{0}' and table_name='{1}'".format(db_name, table_name)
            table_comment = (db.query_sql(sql, 'dict'))[0]['注释']  # 查询数据库表名及注释
            # print(table_comment)
            if table_comment in tables_comment or table_comment == '':     # 判断如果没有重复表就则写入Excel
                continue
            tables_comment.append(table_comment)
            sheet = wbk.add_sheet('{}'.format(table_comment))  # 添加该Excel的第一个sheet
            # add_sheet方法第二个入参cell_overwrite_ok=True
            # 写入第一行：数据表名+注释
            table_name_style = xlwt.XFStyle()  # 初始化样式
            table_name_style.font.bold = True   # 黑体
            table_name_style.font.color = 'black'  # 字体颜色设置为黑色
            table_name_style.font.height = 240  # 字体大小，240就是12号字体
            sheet.write(0, 0, table_comment+' '+table_name, table_name_style)
            # 写入字段名
            style = xlwt.XFStyle()  # 初始化样式
            style.font.color = 'black'  # 字体颜色设置为黑色
            style.font.height = 220  # 字体大小，220就是11号字体
            row_num = 3
            for col_num in range(len(columns)):
                sheet.write(row_num, col_num, columns[col_num], style)
            # 写入字段属性
            for row in range(len(desc)):
                for col in range(len(columns)):
                    # (Modify column width to match biggest data in that column)
                    if (len(str(desc[row][col])) * 367) > sheet.col(col).width:
                        print(desc[row][col])
                        sheet.col(col).width = (len(str(desc[row][col])) * 367)
                    sheet.write(row+row_num+1, col, desc[row][col], style)
            wbk.save(excel_name + '.xls')  # 保存Excel
            i += 1
        print("数据库表保存成功，共{}张表".format(i))
        db.disconnect_db()


class MysqlTools:

    def connect_mysql(self, host, user, passwd, db=None):
        """
        连接Mysql数据库
        :param host: 数据库服务器IP地址
        :param user: 用户名
        :param passwd: 密码
        :param db: 数据库
        """
        # 连接数据库
        self.connect = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=db, charset='utf8')
        if self.connect.open:
            print("数据库连接成功")
            self.cursor = self.connect.cursor()  # 使用cursor方法创建一个游标
            return self.connect, self.cursor
        else:
            print("数据库连接失败")

    def execute_sql(self, sql):
        """
        执行SQL语句
        :param sql: SQL语句
        """
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except:
            self.connect.rollback()

    def disconnect_db(self):
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
            # print(sql)
            self.cursor.execute(sql)
            if return_type == 'tuple':
                result = self.cursor.fetchall()
                return result
            if return_type == 'dict':  # 将查询结果转换为字典
                columns = [desc[0] for desc in self.cursor.description]
                result = [dict(zip(columns, row)) for row in self.cursor]
                return result
        except:
            print(sql)
            self.connect.rollback()

    def query_count(self, sql):
        """
        查询记录数
        :param sql: SQL语句
        :return: self.cursor.rowcount: 查询结果记录数
        """
        self.cursor.execute(sql)
        return self.cursor.rowcount

    def query_table_info(self, db_name, table_name):
        """
        查询数据库表字段及注释
        :param db_name: 数据库名
        :param table_name: 表名
        :return: db_desc_result: 数据库表字段及注释
        """
        sql = "SELECT (@rowNum:=@rowNum+1) as 序号,COLUMN_NAME 列名,COLUMN_TYPE 数据类型,DATA_TYPE 字段类型," \
              "CHARACTER_MAXIMUM_LENGTH 长度,IS_NULLABLE 是否为空,COLUMN_DEFAULT 默认值,COLUMN_COMMENT 备注 " \
              "FROM INFORMATION_SCHEMA.COLUMNS,(SELECT @rownum:=0) r " \
              "WHERE table_schema='{0}' AND table_name='{1}'".format(db_name, table_name)
        db_desc_result = self.query_sql(sql)
        # print(db_desc_result)
        # print(self.query_count(sql))
        return db_desc_result

    def query_table_name(self, db_name):
        """
        查询数据库下所有表名
        :param db_name: 数据库名
        :return: tables_name_list：数据库表名（列表）
        """
        sql = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE table_schema='%s'" % db_name
        tables_name = self.query_sql(sql)
        tables_count = self.query_count(sql)
        print("{0}数据库中共{1}张表".format(db_name, tables_count))
        tables_name_list = []
        for table in tables_name:
            tables_name_list.append(table[0])
        return tables_name_list


if __name__ == '__main__':
    t = DatebaseXls()
    t.dbx_main('数据库设计文档 V1.0')



