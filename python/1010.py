# -*- coding: utf-8 -*-

input_1 = input()
input_2 = input()

values_1 = input_1.split(" ")
values_2 = input_2.split(" ")

total_pay_product_1 = float(values_1[1]) * float(values_1[2])
total_pay_product_2 = float(values_2[1]) * float(values_2[2])

total_pay = total_pay_product_1 + total_pay_product_2
print("VALOR A PAGAR: R$ %.2f" % total_pay)
