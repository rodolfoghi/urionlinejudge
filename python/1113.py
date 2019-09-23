while True:
    x, y = [int(z) for z in input().split()]

    if x == y:
        break
    elif x > y:
        print("Decrescente")
    else:
        print("Crescente")