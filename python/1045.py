# -*- coding: utf-8 -*-

lados = [float(x) for x in input().split(" ")]

lados.sort(reverse=True)
a = lados[0]
b = lados[1]
c = lados[2]

# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
if (a >= b + c):
    print("NAO FORMA TRIANGULO")
else:
    # se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    if (a ** 2 == b ** 2 + c ** 2):
        print("TRIANGULO RETANGULO")

    # se A2 > B2 + C2, apresente a mensgem: TRIANGULO OBTUSANGULO
    if (a ** 2 > b ** 2 + c ** 2):
        print("TRIANGULO OBTUSANGULO")

    # se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    if (a ** 2 < b ** 2 + c ** 2):
        print("TRIANGULO ACUTANGULO")

    # se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    if (a == b and a == c):
        print("TRIANGULO EQUILATERO")

    # se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
    if (a == b and a != c or (b == c and b != a)):
        print("TRIANGULO ISOSCELES")
