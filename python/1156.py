s = 1
i = 3
d = 2

while i <= 39:
    s += i/d
    i += 2
    d = d * 2

print('{:.2f}'.format(s))
