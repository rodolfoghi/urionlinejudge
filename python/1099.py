n = int(input())

for i in range(n):
    x, y = [int(x) for x in input().split()]
    soma = 0
    for z in range(min(x,y) + 1, max(x,y)):
        if (z % 2 != 0):
            soma += z
    print(soma)
