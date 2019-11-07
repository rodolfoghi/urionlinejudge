numero_de_testes = int(input())

for teste in range(0, numero_de_testes):
  entrada = input().split()
  pa = int(entrada[0])
  pb = int(entrada[1])
  g1 = float(entrada[2])/100
  g2 = float(entrada[3])/100
  anos = 0
  while pa <= pb:
    pa += int(pa * g1)
    pb += int(pb * g2)
    anos += 1
    if anos > 100:
      break
  
  if anos <= 100:
    print(anos, 'anos.')
  else:
    print('Mais de 1 seculo.')