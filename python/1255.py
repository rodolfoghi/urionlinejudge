testes = int(input())

for teste in range(testes):
    palavra = input().lower()
    caracteres = {}
    for c in palavra:
        if c.isalpha() and c not in caracteres:
            caracteres[c] = palavra.count(c)

    # Ordenar o dicionário em ordem
    #decrescente de valor e crescente de chave
    caracteres_ordenados = sorted(caracteres.items(), key=lambda x: (-x[1],x[0]))
    maior = caracteres_ordenados[0][1]
    resultado = ''
    for c in caracteres_ordenados:
        if c[1] == maior:
            resultado += c[0]
        else:
            break
    print(resultado)
