n = int(input())

for t in range(n):
    i = input().split()
    h = int(i[0])
    d = int(i[1])
    g = int(i[2])

    if 200 <= h <= 300 and d >= 50 and g >= 150:
        print('Sim')
    else:
        print('Nao')

