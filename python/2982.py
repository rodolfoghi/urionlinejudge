n = int(input())

saldo = 0
for i in range(n):
    valores = input().split()
    t = valores[0]
    c = int(valores[1])
    if t == 'G':
        saldo -= c
    else:
        saldo += c

if saldo >= 0:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')

