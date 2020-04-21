o = input()
matriz = []
t = 12

for l in range(t):
    linha = []
    for j in range(t):
        linha.append(float(input()))
    matriz.append(linha)

linha_inicial = 1
coluna_final = 1
abaixo_diagonal = []

for x in range(linha_inicial, t):
    for j in range(coluna_final):
        abaixo_diagonal.append(matriz[x][j])
    coluna_final += 1

r = 0

if o == 'S':
    r = sum(abaixo_diagonal)
elif o == 'M':
    r = sum(abaixo_diagonal) / len(abaixo_diagonal)

print('{:.1f}'.format(r))
