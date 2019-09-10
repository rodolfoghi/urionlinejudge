# -*- coding: utf-8 -*-

hora_inical, hora_final = [int(x) for x in input().split(" ")]

if hora_final > hora_inical:
    duracao = hora_final - hora_inical
elif hora_inical > hora_final:
    duracao = 24 - hora_inical + hora_final
else:
    duracao = 24

print("O JOGO DUROU {} HORA(S)".format(duracao))