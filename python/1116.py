n = int(input())

for i in range(n):
    x, y = [int(z) for z in input().split()]

    try:
        print(x / y)
    except:
        print("divisao impossivel")