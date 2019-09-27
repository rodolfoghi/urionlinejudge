while True:
    valores = [int(x) for x in input().split()]

    m = min(valores)
    n = max(valores)

    if m <= 0:
        break

    texto = ""
    soma = 0
    for i in range(m, n + 1):
        soma += i
        texto += str(i) + " "

    print("{}Sum={}".format(texto, soma))