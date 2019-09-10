# -*- coding: utf-8 -*-

hora_inicial, minuto_inicial, hora_final, minuto_final = [int(x) for x in input().split(" ")]

horas = hora_final - hora_inicial

if (horas < 0):
    horas += 24

minutos = minuto_final - minuto_inicial

if (minutos < 0):
    minutos += 60
    horas -= 1

if (horas == 0 and minutos == 0):
    horas = 24

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
