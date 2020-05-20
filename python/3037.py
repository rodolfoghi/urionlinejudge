def arremessos():
    pontos = 0

    for a in range(3):
        arremesso = input().split()
        x = int(arremesso[0])
        d = int(arremesso[1])
        pontos += x * d

    return pontos

n = int(input())

for i in range(n):
    pontos_joao = arremessos()
    pontos_maria = arremessos()

    if pontos_joao > pontos_maria:
        print('JOAO')
    else:
        print('MARIA')