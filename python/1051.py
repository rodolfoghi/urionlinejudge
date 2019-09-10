# -*- coding: utf-8 -*-

salario = float(input())

faixa2 = (min(salario, 3000.00) - 2000.00) * 8/100
faixa3 = (min(salario, 4500.00) - 3000.00) * 18/100
faixa4 = (salario - 4500.00) * 28/100

ir = max(faixa2, 0) + max(faixa3, 0) + max(faixa4, 0)

if (ir == 0):
    print("Isento")
else:
    print("R$ {:.2f}".format(ir))
