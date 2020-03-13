def movimenta(posicao_atual, movimento):
  # Trocar o copo na posição A com o copo na posição B.
  if movimento == 1:
    valor1, valor2 = 'A', 'B'
  # Trocar o copo na posição B com o copo na posição C.
  elif movimento == 2:
    valor1, valor2 = 'B', 'C'
  # Trocar o copo na posição A com o copo na posição C.
  elif movimento == 3:
    valor1, valor2 = 'A', 'C'
  
  if posicao_atual == valor1:
    return valor2
  elif posicao_atual == valor2:
    return valor1
  else:
    return posicao_atual



n = int(input())
posicao_atual = input()

for i in range(n):
  movimento = int(input())
  posicao_atual = movimenta(posicao_atual, movimento)

print(posicao_atual)