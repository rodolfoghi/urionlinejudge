x = int(input())
y = int(input())

soma = 0

for i in range(min(x, y) - 1, max(x, y)):
    print("i", i)
    if (i % 2 != 0):
        soma += i

print(soma)
