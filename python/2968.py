import math

# Ler a entrada
entrada = input()
valores = entrada.split()

# Calcular o total de placas (nro de voltas * nro placas)
total_de_placas = int(valores[0]) * int(valores[1])

result = []

# Calcular a qtd de placas para 10%
# Calcular a qtd de placas para 20%
# Calcular a qtd de placas para 30%
#...
# Calcular a qtd de placas para 90%
for i in range(1, 10):
  percentual = i / 10
  qtd_placas = total_de_placas * percentual
  qtd_placas_str = str(math.ceil(qtd_placas))
  result.append(qtd_placas_str)
  
# Imprimir o resultado
result_str = " ".join(result)

print(result_str)