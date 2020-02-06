"""
2020.02.03 题目：
(1)写一个函数，输入一个字符串，返回一个与该字符串大小写反转，而且反序的字符串
(2)写一个函数，输入一个字符串，按顺序取出该字符串中的数字，然后组成新的字符串，如输入"agf23bss43dsfds6fd4",输出"234364"
(3)写一个函数，输入一个字符串和一个字串，统计字串在该字符串中的个数，不区分大小写，如"ab"在"DSabABaBA"中的个数是3
"""

# (1)写一个函数，输入一个字符串，返回一个与该字符串大小写反转，而且反序的字符串
def string_test1(str1):
    return str1.swapcase()[::-1]
str1 = "ubGSHWfb"
print(string_test1(str1))

# (2)写一个函数，输入一个字符串，按顺序取出该字符串中的数字，然后组成新的字符串，
# 如输入"agf23bss43dsfds6fd4",输出"234364"
def string_test2(str1):
    new_str = ""
    for i in str1:
        if i.isdigit():     # 判断字符串是否为数字
            new_str += i
    print(new_str)
    return new_str
string_test2("agf23bss43dsfds6fd4")

# (3)写一个函数，输入一个字符串和一个字串，统计字串在该字符串中的个数，不区分大小写，
# 如"ab"在"DSabABaBA"中的个数是3
def string_test3(str1, str2):
    str_count = str1.lower().count(str2.lower())
    print(str_count)
    return str_count
string_test3("DSabABaBA", "ab")



