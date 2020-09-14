#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:45:36 2020

@author: asrinhaktansahin
"""


#random password generator with random module**

import random

kerning = int(input("How many digits should your password be? : "))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
characters = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

while True:
    ask_letters = input("Does your password contain letters?[Y/N] : ")
    if ask_letters != "Y" and ask_letters != "N":
        print("Incorrect entry - enter Y or N : ")
        continue
    
    while True:
        ask_numbers = input("Does your password contain numbers?[Y/N] : ")
        if ask_numbers != "Y" and ask_numbers != "N":
           print("Incorrect entry - enter Y or N : ")
           continue
        break
    break

if ask_numbers == 'Y':
    list1 = characters + numbers
else:
    list1 = characters
 
if ask_letters == 'Y':
    list1 = list1 + letters
 
password = ''
 
for i in range(kerning):
    password += random.choice(list1)
     
print(password)