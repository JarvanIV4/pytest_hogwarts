class a:
    def index_query_main(self, *args):
        """
        指数查询主方法
        :param benchmark_code: 指数代码
        :param benchmark_name: 指数名称
        :param data_start_dt: 开始时间
        :param data_end_dt: 结束时间
        """
        response = self.index_query(*args)
        print(response)

    def index_query(self, benchmark_code="", benchmark_name="", data_start_dt="", data_end_dt=""):
        a = benchmark_code+benchmark_name+data_start_dt+data_end_dt
        return a
        # return benchmark_code

if __name__ == '__main__':
    a().index_query_main("", "huh", 'eew', "32")