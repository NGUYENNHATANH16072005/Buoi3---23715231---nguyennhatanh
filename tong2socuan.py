# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:38:41 2024

@author: nhat anh
"""
n = int(input("Nhập số nguyên dương n có 2 chữ số: "))
if 10 <= n <= 99:
    chusohangchuc = n // 10
    chusohangdonvi = n % 10
    tongcacchuso = chusohangchuc + chusohangdonvi
    print("Tổng các chữ số của", n, "là:", tongcacchuso)
else:
    print("Số bạn nhập không phải là số nguyên dương có 2 chữ số.")
