# Operação
o = input()

tamanho = 12
matriz = []

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))

    matriz.append(linha)

v = []

coluna = 1
for l in range(tamanho - 1):
    for j in range(coluna, tamanho):
        v.append(matriz[l][j])
    coluna += 1

resultado = 0

if o == 'S':
    resultado = sum(v)
elif o == 'M':
    resultado = sum(v) / len(v)

print('{:.1f}'.format(resultado))
