# -*- coding: utf-8 -*-

a = float(input())
b = float(input())
c = float(input())

avg = ((a * 2.0) + (b * 3.0) + (c * 5.0)) / (2.0 + 3.0 + 5.0)
precision = 1
print("MEDIA = " + "{:.{}f}".format( avg, precision ))
