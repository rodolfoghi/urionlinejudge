while True:

    notas_validas = []

    while len(notas_validas) < 2:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            notas_validas.append(nota)
        else:
            print("nota invalida")

    print("media = {:.2f}".format((sum(notas_validas) / len(notas_validas))))
    notas_validas = []

    valor_lido_invalido = True
    continuar_calculando = True

    while valor_lido_invalido:
        print("novo calculo (1-sim 2-nao)")

        try:
            x = int(input())
        except:
            continue

        if (x == 2):
            valor_lido_invalido = False
            continuar_calculando = False
        if x == 1:
            valor_lido_invalido = False

    if not continuar_calculando:
        break
