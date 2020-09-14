#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:25:57 2020

@author: asrinhaktansahin
"""


#ATM APP

import random

asrinacc = {'name' : 'Asrin Haktan Sahin',
            'accno' : random.randint(1000,10000),
            'balance' : 7500,
            'additional_balance' : 2500
            }
geraltacc = {'name' : 'Geralt of Rivia',
             'accno' : random.randint(1000,10000),
             'balance' : 5000,
             'additional_balance' : 1000
             }
Ciriacc = {'name' : 'Ciri',
           'accno' : random.randint(1000,10000),
           'balance' : 3000,
           'additional_balance' : 500
           }

def withdrawmoney(account,amount):
    print(f"Hello {account['name']}")
    
    if account['balance'] >= amount:
        account['balance'] -= amount
        print(f"you can get your money, your remaining amount is {account['balance']} Dollars!")
    else:
        total = account['balance'] + account['additional_balance']
        if total >= amount:
            tobeused = input("Do you agree that additional accounts will be used? [Y/N]\n : ")
            if tobeused == "Y":
                total -= amount
                print("you can get your money, your remaining amount is", total)
            elif tobeused == "N":
                print(f"sorry we couldn't help {account['name']}")
        elif total < amount:
            print(f"insufficient balance {account['name']}")

withdrawmoney(asrinacc,7000)
withdrawmoney(geraltacc,5500)
withdrawmoney(Ciriacc,4000)