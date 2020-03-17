# -*- coding: utf-8 -*-
# @Time : 2020/03/10
# @Author : Wind

s = 'EROUOHIGVDSFBSBDHFKHKJSN;LDFDIUGUHBIAEAWRVBLBV'
for i in range(len(s)-2):
    l = ''
    if s[i] == s[i+2]:
        l = s[i]+s[i+1]+s[i+2]
        print(l)
