# -*- coding: utf-8 -*-

seller_name = input()
seller_salary = float(input())
total_sold = float(input())

total_salary = seller_salary + (total_sold * 0.15)

print("TOTAL = R$ %.2f" % total_salary)