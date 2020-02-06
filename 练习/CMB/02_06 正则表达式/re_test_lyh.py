import re
import time
import datetime
from dateutil.rrule import *
from dateutil.parser import parse
person_info=[{"name":"张浩","num":"1324"},{"num":"AA11","name":"李天"},{"num":"AA12","name":"王浩"},{"num":"AA15","name":"刘天天"},{"num":"HH23","name":"周浩晨"},{"num":"1151","name":"梁颖"}]
time_info=[{"num":"AA12","start":"2019-10-11","end":"error:can not get message"},{"num":"AA15","start":"2019-11-05","end":"2019-12-03"},{"num":"1324","start":"2019-11-15","end":"9999-12-31"},
{"num":"AA11","start":"2019-12-02","end":"2019-12-07"},{"num":"1151","start":"","end":""},{"num":"HH23","start":"2019-11-07","end":""}]

def count_person(person_info):
    count=0
    for info in person_info:
        name=info.get("name")
        if re.search("天+",name) is not None:
            count+=1
    return count

print(count_person(person_info))

def name_max_char(person_info):
    chinese_list=[]
    count_chin_dict={}
    for info in person_info:
        name=info.get("name")
        for chinese in name:
            if chinese in chinese_list:
                count_chin_dict[chinese]+=1
            else:
                chinese_list.append(chinese)
                count_chin_dict[chinese]=1
    print(count_chin_dict)
    chin_list=count_chin_dict.values()
    max_count=max(chin_list)
    new_dict={}
    for key,value in count_chin_dict.items():
        if value==max_count:
            print(key,max_count,"次")
            new_dict[key]=value
    print(new_dict)
    return new_dict
name_max_char(person_info)

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




