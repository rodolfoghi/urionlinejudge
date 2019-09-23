# -*- coding: utf-8 -*-

leds = {
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
    "0": 6
}

casos = int(input())

for x in range(casos):
    teste = input()
    soma = 0
    for letra in teste:
        soma += int(leds[letra])
    print(soma, "leds")