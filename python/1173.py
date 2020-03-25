valor = int(input())

vetor = []
vetor.append(valor)

for i in range(9):
    valor *= 2
    vetor.append(valor)

for i in range(10):
    print('N[{}] = {}'.format(i, vetor[i]))
