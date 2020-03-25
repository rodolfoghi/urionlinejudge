v = []
tamanho_vetor = 100

for i in range(tamanho_vetor):
    v.append(float(input()))

for i in range(tamanho_vetor):
    if v[i] <= 10:
        print('A[{}] = {:.1f}'.format(i, v[i]))
