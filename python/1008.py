# -*- coding: utf-8 -*-

n = int(input())
worked_hours = int(input())
amout_per_hour = float(input())

salary = worked_hours * amout_per_hour

print("NUMBER = " + str(n))
print("SALARY = U$ " + "{:.{}f}".format( salary, 2 ))
