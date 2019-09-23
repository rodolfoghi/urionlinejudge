# -*- coding: utf-8 -*-

x = int(input())

z = -999999
while z <= x:
    z = int(input())

soma = 0
cont = 0
while soma <= z:
    soma += x
    x += 1
    cont += 1

print(cont)