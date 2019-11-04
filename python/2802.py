# -*- coding: utf-8 -*-
n = int(input())
tomados_dois_a_dois = (n * (n - 1)) / 2
tomados_quatro_a_quatro = (n * (n-1) * (n-2) * (n-3)) / (2 * 3 * 4)
r = 1 + tomados_dois_a_dois + tomados_quatro_a_quatro
print(int(r))