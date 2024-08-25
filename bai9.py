# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:44:11 2024

@author: nhat anh
"""
import math
a = float(input("So thuc a:"))
b = float(input("So thuc b:"))
ve1=math.sqrt(a)-math.sqrt(b)
ve2=a**(1/4)-b**(1/4)
ve3=math.sqrt(a)+(a*b)**(1/4)
ve4=a**(1/4)+b**(1/4)
ketqua=(ve1/ve2)-(ve3/ve4)
print("Ket qua cua bieu thuc la:", ketqua)
