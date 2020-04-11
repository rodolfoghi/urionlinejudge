# -*- coding: utf-8 -*-

def imprimir_vetor(nome, vetor):
    for i in range(len(vetor)):
        print('{}[{}] = {}'.format(nome, i, vetor[i]))


pares = []
impares = []

for i in range(15):
    x = int(input())

    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

    if len(pares) == 5:
        imprimir_vetor('par', pares)
        pares = []

    if len(impares) == 5:
        imprimir_vetor('impar', impares)
        impares = []

if len(impares) > 0:
    imprimir_vetor('impar', impares)

if len(pares) > 0:
    imprimir_vetor('par', pares)
