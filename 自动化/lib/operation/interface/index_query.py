from operation.InterfaceOps import InterfaceOps
from config.interface.index.index_query_conf import IndexQueryConf as Iqc
from datetime import datetime


class IndexQuery(InterfaceOps):

    def __init__(self, user):
        super().__init__()
        Iqc.settings["Cookie"] = self.get_loginCookie(user)

    def index_query_main(self, benchmark_code="", benchmark_name="", data_start_dt="", data_end_dt=""):
        """
        指数查询主方法
        :param benchmark_code: 指数代码
        :param benchmark_name: 指数名称
        :param data_start_dt: 开始时间
        :param data_end_dt: 结束时间
        """
        response = self.index_query(benchmark_code, benchmark_name, data_start_dt, data_end_dt)
        assert self.index_data_check(response)

    def index_query(self, benchmark_code="", benchmark_name="", data_start_dt="", data_end_dt=""):
        """
        指数查询
        :param benchmark_code: 指数代码
        :param benchmark_name: 指数名称
        :param data_start_dt: 开始时间
        :param data_end_dt: 结束时间
        :return: 返回接口响应报文
        """
        Iqc.request_json["benchmark_code"] = benchmark_code
        Iqc.request_json["benchmark_name"] = benchmark_name
        Iqc.request_json["data_start_dt"] = data_start_dt
        Iqc.request_json["data_end_dt"] = data_end_dt
        response = self.send_request(Iqc.api_data, Iqc.settings)    # 发送接口请求
        return response.loads(response.content) # 返回接口响应报文

    def index_status_check(self, response):
        """
        检查指数查询-接口响应报文中的status
        :param response:
        :return:
        """
        real_dict = response["status"]
        expected_dict = {'message': 'OK', 'code': '0'}
        if expected_dict == real_dict:
            return True
        else:
            return False

    def index_count_check(self, response):
        benchmark_code = Iqc.request_json["benchmark_code"]
        benchmark_name = Iqc.request_json["benchmark_name"]
        data_start_dt = Iqc.request_json["data_start_dt"]
        data_end_dt = Iqc.request_json["data_end_dt"]
        count_sql = "SELECT COUNT(1) FROM GAAS.PRO_BENCHMARKS WHERE 1=1 "
        if benchmark_code != "":
            count_sql += "AND BENCHMARK_CODE LIKE '%" + benchmark_code + "%'"
        if benchmark_code != "":
            count_sql += "AND BENCHMARK_NAME LIKE '%" + benchmark_name + "%'"
        if data_start_dt != "":
            count_sql += "AND DATA_START_DT>T0_DATE('%s', 'yyyy-mm-dd')" % data_start_dt
        if data_end_dt != "":
            count_sql += "AND DATA_END_DT<T0_DATE('%s', 'yyyy-mm-dd')" % data_end_dt
        self.log.info(count_sql)
        count_db = (self.query_sql(count_sql))[0][0]
        count_resp = response["data"]["count"]
        if count_db == count_resp:
            print("记录数一致，%d==%d"%(count_db, count_resp))
            return True
        else:
            print("记录数不一致，%d!=%d"%(count_db, count_resp))
            return False

    def index_data_check(self, response):
        flag = True
        self.log.info("指数查询-数据比对")
        response_key = ["benchmarkCode", "benchmarkName", "dataStartDate", "dataEndDate"]
        db_key = ["BENCHMARK_CODE", "BENCHMARK_NAME", "DATA_START_NAME", "DATA_END_NAME"]
        response = response["data"]["pageList"]
        self.log.info(response)
        j = 0
        for resp in response:
            self.log.info("\n正在比对第%d组数据"%(j+1))
            benchmark_code_resp = resp["benchmarkCode"] # 接口响应报文中的指数代码
            sql = "SELECT * FROM GAAS.PRO_BENCHARKS WHERE 1=1 AND BENCHARK_CODE='%s'" % benchmark_code_resp
            self.log.info(sql)
            result_db = (self.query_sql(sql, "dict"))[0]
            for i in range(len(response_key)):
                # 判断数据库查询数据若为时间类型， 则进行格式化后转为字符串，将接口响应报文中的时间戳转为日期格式的字符串
                if type(result_db[db_key[i]]) is datetime:
                    resp[response_key[i]] = str(datetime.fromtimestamp(float(str(resp[response_key[i]])[:3])))
                    result_db[db_key[i]] = str(result_db[db_key[i]])
                if type(result_db[db_key[i]]) is float:
                    resp[response_key[i]] = str(float(resp[response_key[i]]))
                    result_db[db_key[i]] = str(result_db[db_key[i]])
                if result_db[db_key[i]] == resp[response_key[i]]:
                    self.log.info("第%d行数据benchmarkCode=%s的第%d个字段：%s数据一致" % (j+1, benchmark_code_resp, i+1, response_key))
                    continue
                else:
                    flag = False
                    self.log.error("第%d行数据benchmarkCode=%s的第%d个字段：%s数据一致" % (j+1, benchmark_code_resp, i+1, response_key))
                    self.log.error("%s != %s" % (result_db[db_key[i]], resp[response_key[i]]))
                    break
            if not flag:
                break
            j += 1
        if flag:
            self.log.info("共比对%d组数据"%j)
            print("全部数据比对结束-数据正确")
        else:
            print("全部数据比对结束-部分数据错误")
        self.log.info(flag)
        return flag

    def index_query_check(self, response):
        self.connect_gaas_db()  # 连接数据库
        count_flag = self.index_count_check(response)  # 检查接口响应报文.count
        if count_flag:
            status_flag = self.index_status_check(response)  #检查接口响应报文.status
            data_flag = self.index_data_check(response)     #检查接口响应报文.data
            return status_flag and count_flag and data_flag
        else:
            return False  # 若记录数不正确则直接返回False



