# -*- coding: utf-8 -*-

valores = []

for i in range(5):
    valores.append(int(input()))

print(len([x for x in valores if x % 2 == 0]), "valor(es) par(es)")
print(len([x for x in valores if x % 2 != 0]), "valor(es) impar(es)")
print(len([x for x in valores if x > 0]), "valor(es) positivo(s)")
print(len([x for x in valores if x < 0]), "valor(es) negativo(s)")