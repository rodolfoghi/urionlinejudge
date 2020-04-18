l = int(input())
t = input()

tamanho = 12 
matriz = []
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for v in matriz[l]:
    soma += v

resultado = soma
if t == 'M':
    resultado = soma / tamanho

print('{:.1f}'.format(resultado))
