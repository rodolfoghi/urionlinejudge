combustiveis = []
while True:
    combustivel = int(input())
    if combustivel == 4:
        break

    combustiveis.append(combustivel)

print("MUITO OBRIGADO")
print("Alcool:", combustiveis.count(1))
print("Gasolina:", combustiveis.count(2))
print("Diesel:", combustiveis.count(3))
