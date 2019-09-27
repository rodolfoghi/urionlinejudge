a = 0

x, y = [int(z) for z in input().split()]

while a < y:
    linha = ""
    for i in range(x):
        a += 1
        linha += str(a) + " "
    print(linha.rstrip())