# -*- coding: utf-8 -*-
# __author__: Wind
# 2020/10/15 20:20
import pytest


class Add:

    def test_add(number1, number2):
        sum = number1 + number2
        return sum

    # @pytest.mark.parametrize
    def test_div(number1, number2):
        sum = number1 - number2
        return sum


class run_test:
    def setup(self):
        self.a = Add()

    def teardown(self):
        print(self.test_add(1, 2))
