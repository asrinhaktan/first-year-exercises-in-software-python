#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:11:35 2020

@author: asrinhaktansahin
"""

from tkinter import *
 
def numaraEkle():
    al=int(d1.get())+int(d2.get())
    Deger.set(al)
 
pencere = Tk()
Deger=IntVar()
Label(pencere, text="Sayi1").grid(row=0)
Label(pencere, text="Sayi2").grid(row=1)
Label(pencere, text="Sonuc:").grid(row=3)
result=Label(pencere, text="", textvariable=Deger).grid(row=3,column=1)
 
d1 = Entry(pencere)
d2 = Entry(pencere)
 
d1.grid(row=0, column=1)
d2.grid(row=1, column=1)
 
b = Button(pencere, text="Topla", command=numaraEkle)
b.grid(row=0, column=2,columnspan=2)
 
 
mainloop()






























