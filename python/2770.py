# -*- coding: utf-8 -*-
while True:
    try:
        entrada = input().split()
        x = int(entrada[0])
        y = int(entrada[1])
        for i in range(0, int(entrada[2])):
            pci_cliente = input().split()
            xi = int(pci_cliente[0])
            yi = int(pci_cliente[1])
            #if xi <= x and yi <= y or xi <= y and yi <= x:
            if xi * yi <= x * y:
                print('Sim')
            else:
                print('Nao')
    except:
        break