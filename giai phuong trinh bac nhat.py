# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:19:27 2024

@author: ACER
"""

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
if a != 0:
    x  = -b/a
    print ("Nghiệm của phương trình là:", x)
else:
    if b == 0: 
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm")
        
    