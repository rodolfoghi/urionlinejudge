# -*- coding: utf-8 -*-
def fib(n):
    v = [0, 1]

    if n > 1:
        for i in range(2, n + 1):
            f = v[i - 1] + v[i - 2]
            v.append(f)

    return v[n]

t = int(input())

for teste in range(t):
    n = int(input())
    f = fib(n)
    print('Fib({}) = {}'.format(n, f))
