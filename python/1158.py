testes = int(input())

for t in range(0, testes):
  valores = input().split()
  x = int(valores[0])
  y = int(valores[1])
  
  # Se x eh par, somamos 1 a ele 
  if x % 2 == 0:
    x += 1
  
  soma = 0
  for j in range(0, y):
    soma += x
    x += 2
  print(soma)