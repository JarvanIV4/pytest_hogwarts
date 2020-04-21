import datetime


class DatetimeTest:

    def start_date(self, current_date, delta_date):
        """
        计算执行时间前N天的日期
        :param current_date: 执行时间
        :param delta_date: 当前日期偏差天数
        :return: 返回当前日期前N天的日期
        """
        current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")  # 将字符串转换为时间格式
        delta = datetime.timedelta(days=delta_date)  # 当前日期前29天的日期偏差值
        start_date = (current_date + delta).strftime("%Y-%m-%d")  # 计算当前日期前N天的日期
        return start_date


if __name__ == '__main__':
    t = DatetimeTest()
    print(t.start_date("2020-02-07", 5))   # 2020-02-12