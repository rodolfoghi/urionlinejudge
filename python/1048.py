# -*- coding: utf-8 -*-

salario = float(input())

if salario >= 0.00 and salario <= 400.00:
    percentual = 15
elif salario <= 800.00:
    percentual = 12
elif salario <= 1200.00:
    percentual = 10
elif salario <= 2000.00:
    percentual = 7
else:
    percentual = 4

ganho = salario * percentual / 100
print("Novo salario: {:.2f}".format(salario + ganho))
print("Reajuste ganho: {:.2f}".format(ganho))
print("Em percentual: {} %".format(percentual))