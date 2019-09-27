# -*- coding: utf-8 -*-

positivos = 0
soma = 0

for i in range(6):
    n = float(input())
    if (n > 0.0):
        positivos += 1
        soma += n

print(positivos, "valores positivos")
print("{:.1f}".format(soma / positivos))