# -*- coding: utf-8 -*-
# @Time : 2020/05/04
# @Author : Wind

file_name = 'alice.txt'
try:
    with open(file_name) as f_object:
        contents = f_object.read()
except FileNotFoundError:
    msg = "Sorry, the file '" + file_name + "' does not exist."
    print(msg)
