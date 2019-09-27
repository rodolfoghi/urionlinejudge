# -*- coding: utf-8 -*-

palavra = input()

letras = [char for char in palavra]

total_de_letras = len(letras)

dicionario = {}

for letra in letras:
    count_letra = letras.count(letra)
    if (count_letra > 1):
        dicionario.update({letra: count_letra})

dividendo = 1
for i in range(1, total_de_letras + 1):
    dividendo *= i

divisor = 1
for key, val in dicionario.items():
    for i in range(1, val + 1):
        divisor *= i


anagrama = int(dividendo / divisor)

if (anagrama > 10 ** 9 +7):
    print(int(anagrama % 10 ** 9 +7))
else:
    print(anagrama)
