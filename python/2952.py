def custo_beneficio(acao):
    return {
        'A': 1650 - 1700,
        'C': 2000 - 15500,
        'S': 2000 - 1800,
        'M': 1000 - 450,
        'P': 13000,
        'K': 80 - 100,
        'B': 40,
        'N': 0
    }[acao]

n = int(input())

acoes = input().split()

custos_beneficios = []

for acao in acoes:
    custos_beneficios.append(custo_beneficio(acao))

print(custos_beneficios)