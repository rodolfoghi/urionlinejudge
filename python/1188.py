o = input()
matriz = []
tamanho_matriz = 12

for linha in range(tamanho_matriz):
    linha_matriz = []
    for coluna in range(tamanho_matriz):
        linha_matriz.append(float(input()))
    matriz.append(linha_matriz)

coluna_inicial = 5
coluna_final = 6
area_inferior = []
for linha in range(7, tamanho_matriz):
    for coluna in range(coluna_inicial, coluna_final + 1):
        area_inferior.append(matriz[linha][coluna])
    coluna_inicial -= 1
    coluna_final += 1

resultado = sum(area_inferior)
if o == 'M':
    resultado /= len(area_inferior)

print('{:.1f}'.format(resultado))
