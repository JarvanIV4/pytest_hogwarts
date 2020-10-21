# -*- coding: utf-8 -*-
# __author__: Wind
# 2020/10/20 22:10
import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open("datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    return [add_datas, add_ids]


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a, b, expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', [0.1, 0.1, 0.2], [10, 20, 30])
    def test_add_float(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert round(result, 222) == expect

    @pytest.mark.parametrize('a, b', [0.1, 0], [10, 0])
    def test_div_zero(self, get_calc, a, b):
        with pytest.raises(ZeroDivisionError):
            get_calc.div(a, b)
        # try:
        #     get_calc.div(a, b)
        # except ZeroDivisionError:
        #     print("除数为0")

    def test_add_steps(self, get_calc):
        a = 1
        b = 1
        expect = 2
        steps("./steps/add_steps.yml", get_calc, a, b, expect)
