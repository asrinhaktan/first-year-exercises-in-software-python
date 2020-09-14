#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:43:12 2020
@author: asrinhaktansahin
"""

import time
import datetime
print("Please type your text after 3 seconds")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("Go!")
time.sleep(0.2)
before = datetime.datetime.now()

text=input("Type here:")
after = datetime.datetime.now()

speed = after - before
seconds = round(speed.total_seconds(),2)
letter_per_second = round(len(text) / seconds,1)

print("You typed in : {} seconds.".format(seconds))
print("{} letters per second.".format(letter_per_second))
