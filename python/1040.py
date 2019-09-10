# -*- coding: utf-8 -*-
notas = [float(x) for x in input().split(" ")]

media = round((notas[0] * 2 + notas[1] * 3 + notas[2] * 4 + notas[3] * 1) / (2 + 3 + 4 + 1), 1)

print("Media: {}".format(media))

if (media >= 7.0):
    print("Aluno aprovado.")
elif(media < 5.0):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = round(float(input()), 1)
    print("Nota do exame: {}".format(nota_exame))
    media_final = (media + nota_exame) / 2
    if (media_final >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {}".format(media_final))