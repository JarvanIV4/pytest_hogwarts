import cx_Oracle
import pymysql
import logging
import operator       # 运算符模块


class DatabaseTool:
    """数据库公共方法"""

    def connect_to_db(self, db_info):
        """
        连接Oracle数据库
        :param db_info: 数据库连接信息
        :return:
        """
        logging.info("正在连接数据库")
        if db_info['数据库类型'].lower() == 'oracle':
            dsn = cx_Oracle.makedsn(db_info['host'], 1521, service_name=db_info['service_name'])
            self.database = cx_Oracle(db_info['用户名'], db_info['密码'], dsn=dsn, encoding='utf-8', nendogind='utf-8')
        return self.database

    def disconnect_to_db(self):
        logging.info("断开数据库连接")
        self.cursor.close()
        self.database.close()

    def execute_the_sql(self, sql):
        logging.info("数据库语句执行:%s" % sql)
        try:
            self.cursor.execute(sql)
            self.database.commit()
            logging.error("数据库语句执行完成")
        except:
            logging.error("数据库语句执行失败")
            self.database.rollback()

    def query_sql(self, sql, return_type='tuple'):
        """
        查询数据库
        :param sql: 查询SQL语句
        :param return_type: 返回类型-元组('tuple')或字典('dict')
        :return: result:数据库查询结果
        """
        try:
            self.cursor = self.database.cursor()
            self.cursor.execute(sql)
            if return_type == 'tuple':
                result = self.cursor.fetchall()
                return result
            if return_type == 'dict':   # 将查询结果转换为字典
                columns = [desc[0] for desc in self.cursor.description]
                result = [dict(zip(columns, row)) for row in self.cursor]
                return result
        except:
            self.database.rollback()

    def db_query_count(self, db_name, table_name, *query_option):
        sql = ("select * from %s.%s where" + "and".join(query_option))
        sql = sql.strip()[:3] if sql.strip()[:-3] == "and" else sql.strip()
        return len(self.query_sql(sql, 'dict'))

    def get_desc_info(self, filename, hostname):
        """
        获取指定数据库表的字段描述信息
        :param filename: str 表名
        :param hostname: dict 数据库信息
        :return: None or 包含字段名+字段描述的字典
        """
        if filename in self.__table_desc_info_set:
            return self.__table_desc_info_set.get(filename)
        database, table = filename.split(".")
        sql = {
            "SELECT COLUMN_NAME, COMMENTS FROM ALL_COL_COMMENTS "
            "WHERE OWNER='{0}' AND TABLE_NAME='{1}'"
        }.format(database, table)
        res = self.query_sql(sql)
        if not res:
            return None
        result = OrderedDict()
        result.update(((x.items()[0][1], x.items()[1][1]) for x in res))
        self.__table_desc_info_set[filename] = result
        return result

    def query_result_list(self, query_result):
        """
        将查询结果中的多级tuple转换为list返回，例如((PRO_ID,), (ID,))转为['PRO_ID', 'ID']
        :param query_result:
        :return: 转换后的列表
        """
        result_list = []
        for i in query_result:
            result_list.append(i[0])
        return result_list

    def comp_list(self, list_a, list_b):
        """
        比对列表是否一致，找出不同项
        :param list_a: 第1个列表
        :param list_b: 第2个列表
        :return:
        """
        if not operator.eq(list_a, list_b):
            return "列表一致"
        for a in list_a:
            if a not in list_b:
                print("只在第1个列表存在", a)
        for b in list_b:
            if b not in list_a:
                print("只在第2个列表存在", b)


if __name__ == '__main__':
    PBOT_DB_ST = {
        "数据库类型": "Oracle",
        "host": "99.1.1.1",
        "端口号": "1521",
        "用户名": "user",
        "密码": "abc",
        "service_name": "pbotdb"
    }
    db = DatabaseTool()
    db.connect_to_db(PBOT_DB_ST)
    sql = "select * from "
    db.query_sql(sql, 'dict')
