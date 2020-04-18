n = int(input())

x = [int(x) for x in input().split()]
menor = min(x)
print('Menor valor: {}'.format(menor))
indice = x.index(menor) 
print('Posicao: {}'.format(indice))

