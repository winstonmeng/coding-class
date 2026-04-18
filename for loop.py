#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 14:36:38 2025

# @author: winstonmeng
"""

for counter in range(1,11):
    print(counter)
 
    
for counter in [1,11]:
    print(counter)
# # third way of using range()function
# # which is range(start,stop,step)
for counter in range(1,11,2):
    print(counter)
# #second way of using range()function
# #which is range(stop)
for counter in range(11):
    print(counter)
# #first way of using range()function
# #which is range(start,stop)
for counter in range(1,11):
    print(counter)
    
for counter in range (10,101,10):
    print(counter)
# for loop using a list    
for counter  in range(1,11):
    print(counter*10)   
for counter in [1,2,3,4,5,6,7,8,9,10]:
    print(counter)
numbers=[1,2,3,4,5,6,7,8,9,10]
for counter in numbers[0:5]:
    print(counter)