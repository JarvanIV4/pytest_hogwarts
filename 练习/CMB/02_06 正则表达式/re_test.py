"""
2020.02.05
列表、字典与正则表达式处理：
给定一组人员的信息和他们开始工作日期和结束工作日期信息，
person_info:[{"name":"张浩","num":"1324"},{"num":"AA11","name":"李天"},{"num":"AA12","name":"王浩"},{"num":"AA15","name":"刘天天"},{"num":"HH23","name":"周浩晨"},{"num":"1151","name":"梁颖"}]
time_info:[{"num":"AA12","start":"2019-10-11","end":"error:can not get message"},{"num":"AA15","start":"2019-11-05","end":"2019-12-03"},{"num":"1324","start":"2019-11-15","end":"9999-12-31"},
{"num":"AA11","start":"2019-12-02","end":"2019-12-07"},{"num":"1151","start":"","end":""},{"num":"HH23","start":"2019-11-07","end":""}]
要求：
(1)写一个方法，统计名字中带有"天"的人数
(2)写一个方法，统计出所有名字中出现中文字数最多的中文以及其次数，如果不同的中文出现的次数一样多且为最多，那么同样输出，输出形式为：{'X':n, 'X': n}
(3)写一个方法，计算所有人的工作时间天数，去除周末。如果起始时间为空或者结束时间为"9999-12-31，则输出"unknow"；如果结束时间为空，则结束时间为当前日期；如果结束时间输出其他非日期格式(XXXX-XX-XX,X代表0-9的数字)信息，则输出"error",格式如下
[{"name":"张浩","num":"1324","work_days":n},……]，表示天数或者其他信息
"""

import re
# (1)写一个方法，统计名字中带有"天"的人数
person_info = [{"name":"张浩","num":"1324"},{"num":"AA11","name":"李天"},{"num":"AA12","name":"王浩"},{"num":"AA15","name":"刘天天"},{"num":"HH23","name":"周浩晨"},{"num":"1151","name":"梁颖"}]
# 方法1
def count_tian1(list1):
    count = len(re.findall(r'天+', str(list1)))
    print("名字中带有'天'的人数: " + str(count) + "人")
count_tian1(person_info)
# 方法2
def count_tian2(list1):
    count = 0
    for info in list1:
        num = len(re.findall("天+", info["name"]))
        count += num
    print("名字中带有'天'的人数: " + str(count) + "人")
count_tian2(person_info)
# 方法3
def count_tian3(list1):
    count = 0
    for info in list1:
        if re.search("天+", info["name"]) is not None:
            print("名字中带有'天'的人信息:", str(info))
            count += 1
    print("名字中带有'天'的人数: " + str(count) + "人")
count_tian3(person_info)


# (2)写一个方法，统计出所有名字中出现中文字数最多的中文以及其次数，如果不同的中文出现的次数一样多且为最多，那么同样输出，输出形式为：{'X':n, 'X': n}
def count_zh1(list1):
    for info in list1:
        info
count_zh1(person_info)

# (3)写一个方法，计算所有人的工作时间天数，去除周末。如果起始时间为空或者结束时间为"9999-12-31，则输出"unknow"；如果结束时间为空，则结束时间为当前日期；如果结束时间输出其他非日期格式(XXXX-XX-XX,X代表0-9的数字)信息，则输出"error",格式如下
# [{"name":"张浩","num":"1324","work_days":n},……]，表示天数或者其他信息
time_info = [{"num":"AA12","start":"2019-10-11","end":"error:can not get message"},{"num":"AA15","start":"2019-11-05","end":"2019-12-03"},{"num":"1324","start":"2019-11-15","end":"9999-12-31"},
{"num":"AA11","start":"2019-12-02","end":"2019-12-07"},{"num":"1151","start":"","end":""},{"num":"HH23","start":"2019-11-07","end":""}]


