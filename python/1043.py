# -*- coding: utf-8 -*-

a, b, c = [float(x) for x in input().split(" ")]

forma_triangulo = a + b > c and a + c > b and b + c > a

if forma_triangulo:
    print("Perimetro = {:.1f}".format(a + b + c))
else:
    area = ((a + b) / 2) * c
    print("Area = {:.1f}".format(area))