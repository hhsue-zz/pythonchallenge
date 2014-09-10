#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open("/tmp/tmp.txt", "rb")
str = f.read()
dict = {}
for i in str:
    if i not in dict: 
        print i, ": not found. adding it!" 
        dict[i] = 1
    else:
        print i, ": found!. adding 1"
        dict[i] = dict[i] + 1

print dict

lst = []
result = ''
for i in str:
    if dict[i] == 1:
        result = result + i

print result




