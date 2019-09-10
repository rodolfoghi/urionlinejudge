# -*- coding: utf-8 -*-
import math

# Leia 3 valores de ponto flutuante
a, b, c = [float(x) for x in input().split(" ")]

# e efetue o cálculo das raízes da equação de Bhaskara.
try:
    delta = b * b - 4 * a * c
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)

    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))
# Se não for possível calcular as raízes, mostre a
# mensagem correspondente “Impossivel calcular”,
# caso haja uma divisão por 0 ou raiz de numero negativo.
except:
    print("Impossivel calcular")