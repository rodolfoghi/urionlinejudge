# -*- coding: utf-8 -*-

t = 1
while True:
    x1, y1, x2, y2 = [int(x) for x in input().split()]

    if x1 + y1 + x2 + y2 == 0:
        break

    r = 0
    n = int(input())
    for i in range(n):
        x, y = [int(x) for x in input().split()]
        if x >= x1 and x <= x2 and y <= y1 and y >= y2:
            r += 1

    print('Teste', t)
    print(r)
    t += 1
