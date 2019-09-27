# -*- coding: utf-8 -*-

dia_inicio = int(input().split()[1])
momento_inicio = [int(x) for x in input().split(":")]

dia_fim = int(input().split()[1])
momento_fim = [int(x) for x in input().split(":")]

dias = dia_fim - dia_inicio

horas = momento_fim[0] - momento_inicio[0]

if (horas < 0):
    horas += 24
    dias -= 1

minutos = momento_fim[1] - momento_inicio[1]

if (minutos < 0):
    minutos += 60
    horas -= 1

segundos = momento_fim[2] - momento_inicio[2]

if (segundos < 0):
    segundos += 60
    minutos -= 1

print(dias, "dia(s)")
print(horas, "hora(s)")
print(minutos, "minuto(s)")
print(segundos, "segundo(s)")