x = int(input())
y = int(input())

for i in range(min(x, y) + 1, max(x, y)):
    r = i % 5
    if r == 2 or r == 3:
        print(i)
