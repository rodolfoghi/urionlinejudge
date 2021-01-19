# -*- coding: utf-8 -*-
a, b = map(int, input().split())

r = a % abs(b)
q = (a + (r * -1)) / b
q = int(q)
print(q, r)