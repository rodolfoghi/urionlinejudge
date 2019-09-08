horas_gastas_viagem = int(input())
velocidade_media = int(input())
km_de_viagem = velocidade_media * horas_gastas_viagem
km_por_litro = 12
quantidade_litros_necessaria = km_de_viagem / km_por_litro

print('{:.3f}'.format(quantidade_litros_necessaria))