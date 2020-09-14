#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:45:13 2020

@author: asrinhaktansahin
"""


#salary increase**
#Employees with less than 4000 salaries will receive a 20 percent increase, a 15 percent increase between 4000 and 6000, and a 10 percent increase with a salary of more than 6000.

salary = [3000,5000,7000,2500,4500,10000,3900,6200]
new_salary = []
def salary_increase10(value1):
    print(value1*10/100 + value1)
    return
def salary_increase15(value2):
    print(value2*15/100 + value2)
    return
def salary_increase20(value3):
    print(value3*20/100 + value3)
    return

for i in salary:
    if i < 4001:
        salary_increase20(i)
        
    if i > 4000 and i < 6001:
        salary_increase15(i)
        
    if i >6000:
        salary_increase10(i)
        
    
        
