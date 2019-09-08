segundos_de_duracao_evento = int(input())

h = int(segundos_de_duracao_evento / (60 * 60))
total_segundos_h = h * 60 * 60
m = int((segundos_de_duracao_evento - total_segundos_h) / 60)
total_segundos_m = m * 60
s = int(segundos_de_duracao_evento - total_segundos_h - total_segundos_m)

print(h, m, s, sep=':')