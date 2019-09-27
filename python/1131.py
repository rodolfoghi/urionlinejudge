repeticao = 1
vitorias_inter = 0
vitorias_gremio = 0
empates = 0

while repeticao == 1:
    gols_inter, gols_gremio = [int(g) for g in input().split()]

    if gols_inter > gols_gremio:
        vitorias_inter += 1
    elif gols_gremio > gols_inter:
        vitorias_gremio += 1
    else:
        empates += 1

    print("Novo grenal (1-sim 2-nao)")
    repeticao = int(input())

print("{} grenais".format(vitorias_inter + vitorias_gremio + empates))
print("Inter:{}".format(vitorias_inter))
print("Gremio:{}".format(vitorias_gremio))
print("Empates:{}".format(empates))

if vitorias_inter > vitorias_gremio:
    print("Inter venceu mais")
elif vitorias_inter < vitorias_gremio:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
