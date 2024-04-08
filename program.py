# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:02:09 2023

@author: Ajay
"""

a=int(input())
b=int(input())
if a<b:
    print("the result is:",a)
else:
    c=a//b
    c=a-(b*c)
    print(c)
