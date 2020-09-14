#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:29:14 2020

@author: asrinhaktansahin
"""

#Christmas tree
line = int(input("enter the number of lines : "))
for i in range(line):
    print(' '*(line-i-1) + '*'*(2*i+1))
#----------------------------------------------------------------------------#    
#Rectangular
line = int(input("enter the number of rectangular lines : "))
column = int(input("enter the number of rectangular columns : "))
for line in range(1,line+1):
  for column in range(1,column+1):
    print("*", end=" ")
  print()
#----------------------------------------------------------------------------#
#Right Triangle
line = int(input("enter the number of lines : "))
for number in range(1,line+1,1):
  print(number*"*")
#----------------------------------------------------------------------------#
#Turtle Module
import turtle
 
window=turtle.Screen()
window.bgcolor("green")
 
turtle.color("red")
turtle.circle(150)

