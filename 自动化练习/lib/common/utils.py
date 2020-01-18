class Utils:
    """数据比对"""

    @staticmethod
    def equal_as_integer(real_val, exp_val, *args, **kwargs):
        """
        比对整数
        :param real_val: 实际值
        :param exp_val: 预期值
        :param args:
        :param kwargs:
        """
        return int(exp_val) == int(real_val), "{:d}".format(int(exp_val))

    @staticmethod
    def equal_as_float2(real_val, exp_val, ndigits=2, *args, **kwargs):
        """
        比对浮点数
        :param real_val: 实际值
        :param exp_val: 预期值
        :param args: 精度
        :param args:
        :param kwargs:
        """
        exp_val = round(float(exp_val), ndigits)
        print("精度：", ndigits)
        return exp_val == round(float(real_val), ndigits), "{{:.{}f}}".format(ndigits).format(exp_val)

    @staticmethod
    def equal_within_tolerance(actual_value, expect_value, tolerance, *args, **kwargs):
        """
        容忍度内相等
        :param expect_value: 实际值
        :param expect_value: 预期值
        :param tolerance: 容忍度
        :param args:
        :param kwargs:
        :return: [tuple]=(boolean, )比较结果，展示预期值
        """
        try:
            actual_value = float(actual_value)
            expect_value = float(expect_value)
            tolerance = float(tolerance)
        except Exception as e:
            raise Exception("请确认参数数据类型是否为浮点类型或可以float()")
        delta = abs(actual_value - expect_value)
        return delta < tolerance, (expect_value, tolerance)


if __name__ == '__main__':
    t = Utils()
    print(t.equal_as_integer(8, 9))
