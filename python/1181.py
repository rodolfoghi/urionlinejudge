linha = int(input())
operacao = input()

matriz = []
tamanho = 12 
for i in range(tamanho):
    valores_linha = []
    for i in range(tamanho):
        valor = float(input())
        valores_linha.append(valor)
    matriz.append(valores_linha)

linha_resultado = matriz[linha]
soma = 0
for v in linha_resultado:
    soma += v

resultado = soma
if operacao == 'M':
    resultado = soma / tamanho 

print('{:.1f}'.format(resultado))

