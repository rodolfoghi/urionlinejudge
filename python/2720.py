# -*- coding: utf-8 -*-
numero_de_casos_de_teste = int(input())

for caso_de_teste in range(numero_de_casos_de_teste):
    d = {}
    n, k = [int(x) for x in input().split()]
    for i in range(n):
        i, h, w, l = [int(x) for x in input().split()]
        d[i] = h * w * l

    r = []
    for p in sorted(d.items(), key=lambda x: (-x[1],x[0]))[:k]:
        r.append(p[0])
    print(*r)