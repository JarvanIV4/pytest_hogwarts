import re
string1="LiuYongHua"
def reverse_string(str):
    revers_str=str[::-1]
    revers_list=[]
    for i in range(len(revers_str)):
        if revers_str[i]==revers_str[i].upper():
            revers_list.append(revers_str[i].lower())
        else:
            revers_list.append(revers_str[i].upper())
    return ''.join(revers_list)
#print(reverse_string(string1))
string2="agf23bss43dsfds6fd4"
def new_num_str(str):
    new_list=[]
    for char in str:
        if char>="0" and char<="9":
            new_list.append(char)
    return "".join(new_list)
#print(new_num_str(string2))
string3="DSabABaassBA"
string4="ab"
def count_str(str1,str2):
    str1=str1.upper()
    str2=str2.upper()
    count=str1.count(str2)
    return count
print(count_str(string3,string4))