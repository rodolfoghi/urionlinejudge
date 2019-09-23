# -*- coding: utf-8 -*-

while True:
    x = int(input())
    if x == 0:
        break
    
    valores = []
    for i in range(x):
        valores.append(i + 1)
    
    print(*valores)