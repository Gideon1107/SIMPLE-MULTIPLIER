#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 11:41:45 2022

@author: gideon
"""

"""selectedable multiplication table"""
import time
print("Welcome to Gideon's Multiplier")
print("=============================")
# print('\x1B[3mLOADING\x1B[0m', end = '')
time.sleep(0.3),print('\x1B[3mL', end = ''),time.sleep(0.2),print('\x1B[3m0', end = ''),time.sleep(0.2),print('\x1B[3mA', end = ''),time.sleep(0.2),print('\x1B[3mD', end = ''),time.sleep(0.2),print('\x1B[3mI', end = ''),time.sleep(0.2),print('\x1B[3mN', end = ''),time.sleep(0.2),print('\x1B[3mG\x1B[0m', end = ''),time.sleep(0.3),print('.', end = ''),time.sleep(0.3),print('.', end = ''),time.sleep(0.3),print('.', end = ''),time.sleep(0.3),print('.', end = ''),time.sleep(0.4),print('.')
def multiplier():
    time.sleep(1)
    num = int(input('Desired multiplication table of ?: '))
    end = int(input('To stop multiplying at ?: '))
    print('===============================')
    print('MULTIPLICATION TABLE OF',num)
    print('===============================')
    for i in range(1, end+1):
        print(num,'x', i,  '=', num*i )
    print('===============================')
    print('Thanks for using our multiplier')
    print('===============================')
    time.sleep(2)
    print("DO YOU WANT TO USE THE MULTIPLIER AGAIN? \nIF YES Enter 'Y', IF NO Enter 'N'")
    choice = str(input(""))
    if choice == "Y":
        multiplier()
    elif choice == 'y':
        multiplier()
    else:
        print("THANKS FOR USING OUR MULTIPLIER, SEE YOU ANOTHER TIME")
            
multiplier()
    