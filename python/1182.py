c = int(input())
t = input()

tamanho = 12
matriz = []
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)

coluna = []
for x in range(tamanho):
    coluna.append(matriz[x][c])


resultado = 0

if t == 'S':
    resultado = sum(coluna)
else:
    resultado = sum(coluna) / len(coluna)

print('{:.1f}'.format(resultado))
