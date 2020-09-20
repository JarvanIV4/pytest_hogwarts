# -*- coding: utf-8 -*-
# @Time : 2020/04/21
# @Author : Wind
from collections import OrderedDict


test = OrderedDict()    # OrderedDict实例记录键值对的添加顺序
test['A'] = 'Python'
test['B'] = 'C'
test['C'] = 'Java'
test['D'] = 'C#'

for key, value in test.items():
    print(key + ': ' + value)