idade_em_dias = int(input())

anos = int(idade_em_dias / 365)
meses = int((idade_em_dias - anos * 365) / 30)
dias = int((idade_em_dias - (anos * 365) - (meses * 30)))

print(anos, 'ano(s)')
print(meses, 'mes(es)')
print(dias, 'dia(s)')