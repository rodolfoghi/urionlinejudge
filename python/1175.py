v = []
tamanho_vetor = 20

for i in range(tamanho_vetor):
    v.append(int(input()))

for i in range(int(tamanho_vetor/2)):
    primeiro = v[i]
    ultimo = v[(i+1)*-1]
    v[i] = ultimo
    v[(i+1)*-1] = primeiro

for i in range(tamanho_vetor):
    print('N[{}] = {}'.format(i, v[i]))
