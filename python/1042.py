# -*- coding: utf-8 -*-

valores = [int(x) for x in input().split(" ")]

ordem_lidos = valores.copy()

valores.sort()

for v in valores:
    print(v)

print()

for v in ordem_lidos:
    print(v)