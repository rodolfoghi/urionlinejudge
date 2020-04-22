# Ler a operação
o = input()

# Ler a matriz M[12][12]
matriz = []
tamanho = 12

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)


# Calcular
v = []

for l in range(tamanho - 1):
    for c in range(11 - l):
        v.append(matriz[l][c])

resultado = 0

if o == 'S':
    resultado = sum(v)
elif o == 'M':
    resultado = sum(v) / len(v)

print('{:.1f}'.format(resultado))
