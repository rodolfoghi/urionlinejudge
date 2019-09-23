# -*- coding: utf-8 -*-

while True:
    a, b = input().split()

    if int(a) == 0 and int(b) == 0:
        break

    try:
        print(int(b.replace(a, "")))
    except:
        print(0)
