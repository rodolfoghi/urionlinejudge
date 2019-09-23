senha_correta = 2002

while True:
    senha_lida = int(input())
    if senha_lida == senha_correta:
        print("Acesso Permitido")
        break
    print("Senha Invalida")