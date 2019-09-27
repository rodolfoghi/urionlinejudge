# -*- coding: utf-8 -*-

numero_de_elementos = int(input())
elementos = [int(x) for x in input().split()]

soma = 0
for e in elementos:
    soma += e

rangel = 0

for e in elementos:
    if rangel + e <= soma / 2:
        rangel += e

print(soma - rangel - rangel)

