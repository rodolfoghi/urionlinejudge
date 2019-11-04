# Leia 4 valores inteiros A, B, C e D.
valores_lidos = input()

valores_int = [int(x) for x in valores_lidos.split(' ')]
a = valores_int[0]
b = valores_int[1]
c = valores_int[2]
d = valores_int[3]

# A seguir, se B for maior do que C
valido = b > c

#  e se D for maior do que A,
valido = valido and d > a

# e a soma de C com D for maior que a soma de A e B
valido = valido and c + d > a + b

#  e se C e D, ambos, forem positivos
valido = valido and c > 0 and d > 0
#  e se a variável A for par
valido = valido and a % 2 == 0

# escrever a mensagem "Valores aceitos",
# senão escrever "Valores nao aceitos".
if valido:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')