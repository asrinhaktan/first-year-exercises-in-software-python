#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:02:51 2020

@author: asrinhaktansahin
"""


#map & filter & reduce 

list1 = [1,2,3,4,5]

for i in list1:
    print(i+ 5)


list(map(lambda x: x*20, list1))

#filter

list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

list(filter(lambda x: x % 2 == 0, list2))

#reduce

from functools import reduce

list3 = [1,2,3,4,5,6,7,8,9]
reduce(lambda a,b: a + b, list3)