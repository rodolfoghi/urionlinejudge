# -*- coding: utf-8 -*-

n = int(input())

valores = [0 , 1]
if n > 2:
    for i in range(n - 2):
        soma = valores[len(valores) - 1] + valores[len(valores) - 2]
        valores.append(soma)

print(*valores)