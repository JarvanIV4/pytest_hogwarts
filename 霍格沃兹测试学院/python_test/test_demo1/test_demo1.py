# -*- coding: utf-8 -*-
# __author__: Wind
# 2020/11/4 20:24
import pytest
import yaml


class TestData:

    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yaml")))
    def test_yaml(self, env):
        print("测试环境地址是：" + env["dev"])
