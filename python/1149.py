# -*- coding: utf-8 -*-
valores = input().split()
a = int(valores[0])
n = int(valores[len(valores) - 1])

soma = 0

for i in range(0, n):
    soma += a + i

print(soma)