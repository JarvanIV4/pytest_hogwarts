# -*- coding: utf-8 -*-
# @Time : 2020/05/10
# @Author : Wind

# Python中的for循环，除了可以遍历元素外，还可以进行列表推导。
# 列表推导是一种简化代码的优美方法。推导式是可以从一个数据序列构建另一个新的数据序列的结构体。语法结构为：
# [表达式 for 变量 in 列表] 或者 [表达式 for 变量 in 列表 if 条件]

# 获取新列表
l1 = [data for data in range(1, 5)]
print(l1)  # [1, 2, 3, 4]

# 两个列表内容
v1 = [10, 20, 30]
v2 = [30, 40, 50]
v = [num for num in v1 if num in v2]  # 获取交集
print(v)  # [30]
v = [num for num in v1 if num not in v2]  # 获取差集
print(v)  # [10, 20]