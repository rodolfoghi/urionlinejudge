# -*- coding: utf-8 -*-
t = int(input())

values = []
length = 1000

for i in range(length):
    for j in range(t):
        values.append(j)

for i in range(length):
    print('N[{}] = {}'.format(i, values[i]))
