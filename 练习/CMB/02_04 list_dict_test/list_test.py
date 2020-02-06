"""
2020.02.04 题目：
（1）列表处理：给出一个整数，返回代表该值反序的英文，比如输入89返回英文"nine-eight",该数字限定在0-1000之间，数字之间用"-"隔开
（2）列表与字典处理：给定两个列表，前一个列表中的元素值为数字，后一个列表中的元素值为字符串，要求输出一个字典，该字典的键为第一个列表的数字，值为第二个列表的字符串，字符串长度等于数字的值，且该字符串是第二个列表中最后一个长度满足该数字的字符串
      比如输入[4,7,2,5,9]和["f","43","f2","fgde32e","4322","34aasdasa"],输出{2:"f2",4:"4322",7:"fgde32e",9:"34aasdasa"}
（3）列表与字典处理：输入一个列表，该列表的元素为字典，该字典包含员工的姓名和工号信息，要求输出一个列表，按这些员工名字升序，再按照工号降序排列。
     比如输入[{"name":"Jack","num":"1324"},{"num":"AA11","name":"Liu"},{"num":"AA12","name":"Johnson"},{"num":"AA21","name":"Johnson"},{"num":"HH23","name":"Johnson"},{"num":"1151","name":"Li"}]，
 	 输出[{'name': 'Jack', 'num': '1324'}, {'num': 'HH23', 'name': 'Johnson'}, {'num': 'AA21', 'name': 'Johnson'}, {'num': 'AA12', 'name': 'Johnson'}, {'num': '1151', 'name': 'Li'}, {'num': 'AA11', 'name': 'Liu'}]
"""

# （1）列表处理：给出一个整数，返回代表该值反序的英文，比如输入89返回英文"nine-eight",
#       该数字限定在0-1000之间，数字之间用"-"隔开
def ttt(int1):
    if 0 <= int1 < 1000:
        num_dict = {
            "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
            "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
        }
        num_str = ""
        for i in (str(int1))[::-1]:
            num_str += num_dict[i] + "-"
        print(num_str[:-1])
    else:
        print("数字限定在0-1000之间,请重新输入")
ttt(164)

# （2）列表与字典处理：给定两个列表，前一个列表中的元素值为数字，后一个列表中的元素值为字符串，要求输出一个字典，
# 该字典的键为第一个列表的数字，值为第二个列表的字符串，字符串长度等于数字的值，且该字符串是第二个列表中最后一个长度满足该数字的字符串
# 比如输入[4,7,2,5,9]和["f","43","f2","fgde32e","4322","34aasdasa"],输出{2:"f2",4:"4322",7:"fgde32e",9:"34aasdasa"}
def list_test(list1, list2):
    dict1 = {}
    for list1_num in list1:
        for list2_str in list2:
            if len(list2_str) == list1_num:
                dict1[list1_num] = list2_str
    print(dict1)
list1 = [4, 7, 2, 5, 9]
list2 = ["f", "43", "f2", "fgde32e", "4322", "34aasdasa"]
list_test(list1, list2)

# （3）列表与字典处理：输入一个列表，该列表的元素为字典，该字典包含员工的姓名和工号信息，要求输出一个列表，按这些员工名字升序，再按照工号降序排列。
#    比如输入[{"name":"Jack","num":"1324"},{"num":"AA11","name":"Liu"},{"num":"AA12","name":"Johnson"},{"num":"AA21","name":"Johnson"},{"num":"HH23","name":"Johnson"},{"num":"1151","name":"Li"}]，
# 	 输出[{'name': 'Jack', 'num': '1324'}, {'num': 'HH23', 'name': 'Johnson'}, {'num': 'AA21', 'name': 'Johnson'}, {'num': 'AA12', 'name': 'Johnson'}, {'num': '1151', 'name': 'Li'}, {'num': 'AA11', 'name': 'Liu'}]
def list_desc(list1):
    list_new = sorted(list3, key=lambda x: x["name"], reverse=False)    # 员工名字升序
    # 按工号降序排列
    for j in range(len(list_new)-1):
        for i in range(len(list_new)-j-1):
            if list_new[i]["name"] == list_new[i+1]["name"] and list_new[i]["num"] < list_new[i+1]["num"]:
                list_new[i],list_new[i+1] = list_new[i+1],list_new[i]
    print(list_new)
list3 = [{"name": "Jack", "num": "1324"}, {"num": "AA11", "name": "Liu"}, {"num": "AA12", "name": "Johnson"},
         {"num": "AA21", "name": "Johnson"}, {"num": "HH23", "name": "Johnson"}, {"num": "1151", "name": "Li"}]
list_desc(list3)