notas_validas = []

while len(notas_validas) < 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        notas_validas.append(nota)
    else:
        print("nota invalida")

print("media =", sum(notas_validas) / 2)
