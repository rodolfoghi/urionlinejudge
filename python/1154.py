# -*- coding: utf-8 -*-

idades = []

while True:
    idade = int(input())

    if idade < 0:
        break

    idades.append(idade)

media_de_idade = sum(idades) / len(idades)
print("{:.2f}".format(media_de_idade))