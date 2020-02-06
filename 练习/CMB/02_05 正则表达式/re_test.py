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
import time
from dateutil.rrule import *
from dateutil.parser import parse
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


# (2)写一个方法，统计出所有名字中出现中文字数最多的中文以及其次数，
# 如果不同的中文出现的次数一样多且为最多，那么同样输出，输出形式为：{'X':n, 'X': n}
def ch_count_max(list1):
    chinese = []
    ch_count_dict = {}
    for ch in list1:
        for ch in ch["name"]:
            if ch in chinese:
                ch_count_dict[ch] += 1
            else:
                chinese.append(ch)
                ch_count_dict[ch] = 1
    max_count = max(ch_count_dict.values())
    print(max_count)
    ch_count_max_dict = {}
    for key, value in ch_count_dict.items():
        if value == max_count:
            ch_count_max_dict[key] = max_count
    print(ch_count_max_dict)
ch_count_max(person_info)

# (3)写一个方法，计算所有人的工作时间天数，去除周末。如果起始时间为空或者结束时间为"9999-12-31，则输出"unknow"；如果结束时间为空，则结束时间为当前日期；如果结束时间输出其他非日期格式(XXXX-XX-XX,X代表0-9的数字)信息，则输出"error",格式如下
# [{"name":"张浩","num":"1324","work_days":n},……]，表示天数或者其他信息
time_info = [{"num":"AA12","start":"2019-10-11","end":"error:can not get message"},{"num":"AA15","start":"2019-11-05","end":"2019-12-03"},{"num":"1324","start":"2019-11-15","end":"9999-12-31"},
{"num":"AA11","start":"2019-12-02","end":"2019-12-07"},{"num":"1151","start":"","end":""},{"num":"HH23","start":"2019-11-07","end":""}]
def count_work_days(person_info,time_info):
    for i in range(len(person_info)):
        info=person_info[i]
        for person_time_info in time_info:
            if info.get("num")==person_time_info.get("num"):
                work_days=0
                start=person_time_info.get("start")
                end=person_time_info.get("end")
                if start.strip()=="" or end.strip()=="9999-12-31":
                    work_days="unknow"
                elif end.strip()=="":
                    end=time.strftime("%Y-%m-%d", time.localtime())
                elif re.search("[0-9]{4}\-[0-9]{2}\-[0-9]{2}",end) is None:
                    work_days="error"
                if work_days==0:
                    work_days=rrule(DAILY,dtstart=parse(start),until=parse(end),byweekday=(MO,TU,WE,TH,FR)).count()
                print("work_days:",work_days,"start:",start,"end:",end)
                print("num:",info.get("num"),work_days)
                person_info[i]["work_days"]=work_days
                break
    print(person_info)
    return person_info
count_work_days(person_info,time_info)

