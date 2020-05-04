# -*- coding: utf-8 -*-
# @Time : 2020/05/04
# @Author : Wind
import json

numbers = [2, 3, 5, 7, 11, 13]
file_name = 'numbers.json'
with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)

# 读取
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

