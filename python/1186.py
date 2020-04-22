o = input()

matriz = []
tamanho = 12

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)

v = []

for l in range(1, tamanho):
    for c in range(tamanho-l, tamanho):
        v.append(matriz[l][c])

resultado = 0
if o == 'S':
    resultado = sum(v)
elif o == 'M':
    resultado = sum(v) / len(v)

print('{:.1f}'.format(resultado))
