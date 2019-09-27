# -*- coding: utf-8 -*-

n = int(input())

fat = 1
while n > 1:
    fat = fat * n
    n = n - 1

print(fat)