# -*- coding: utf-8 -*-

a = float(input())
b = float(input())

avg = ((a * 3.5) + (b * 7.5)) / (3.5 + 7.5)

print("MEDIA = " + "{:.{}f}".format( avg, 5 ))
