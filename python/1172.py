x = []

for i in range(10):
    valor = int(input())
    if valor <= 0:
        valor = 1
    x.append(valor)

for i in range(10):
    print('X[{}] = {}'.format(i, x[i]))
