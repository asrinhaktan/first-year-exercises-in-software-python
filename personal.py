#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:48:15 2020

@author: asrinhaktansahin
"""


class personal:
    def __init__(self, name, position, salary, experience_year):
        self.name = name
        self.position = position
        self.salary = salary
        self.experience_year = experience_year

p1 = personal("Mehmet", "datascientist", 5000, 3)
p2 = personal("John", "NetworkSpecialist", 6000, 5)
p3 = personal("Michael", "Secretary", 2000, 2)
p4 = personal("Albert", "SoftwareDev", 7000, 8)

print(p1.name)
print(p2.name, p2.position, p2.salary, p2. experience_year)
print(p3.salary,p3.experience_year)
        
        