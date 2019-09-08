def calcula_notas_de(valor_nota, valor_total):
    qtd_notas = int(valor_total / valor_nota)
    print(qtd_notas, ' nota(s) de R$ ', valor_nota, ',00',  sep='')
    return qtd_notas * valor_nota


valor_informado = int(input())

print(valor_informado)

valor_ja_contabilizado = calcula_notas_de(100, valor_informado)
valor_ja_contabilizado += calcula_notas_de(50,
                                           valor_informado - valor_ja_contabilizado)
valor_ja_contabilizado += calcula_notas_de(20,
                                           valor_informado - valor_ja_contabilizado)
valor_ja_contabilizado += calcula_notas_de(10,
                                           valor_informado - valor_ja_contabilizado)
valor_ja_contabilizado += calcula_notas_de(5,
                                           valor_informado - valor_ja_contabilizado)
valor_ja_contabilizado += calcula_notas_de(2,
                                           valor_informado - valor_ja_contabilizado)
calcula_notas_de(1, valor_informado - valor_ja_contabilizado)
