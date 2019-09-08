# Ler a quantidade total de segundos
tempo_total = int(input())

# Calcular horas, minutos e segundos
quantidade_segundos = [3600, 60, 1]
resultado = []

for alvo in quantidade_segundos:
    qtd = int(tempo_total / alvo)
    resultado.append(str(qtd))
    tempo_total -= qtd * alvo

# Imprimir o resultado
print(":".join(resultado))