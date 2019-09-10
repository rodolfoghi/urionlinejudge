# -*- coding: utf-8 -*-
codigo, quantidade = [int(x) for x in input().split(" ")]

precos = [4.00, 4.50, 5.00, 2.00, 1.50]

total = precos[codigo -1] * quantidade

print("Total: R$ {:.2f}".format(total))
