# -*- coding: utf-8 -*-
# @Time : 2020/05/04
# @Author : Wind

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        if second_number == 'q':
            break
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)