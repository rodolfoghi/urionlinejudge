'''
Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:

Input

The input file contains 3 integer values.
Output

Print the greatest of these three values followed by a space and the message "eh o maior".
'''
# -*- coding: utf-8 -*-

values = input().split(" ")

maior = 0

for value in values:
    if (int(value) > maior):
        maior = int(value)

print(str(maior) + " eh o maior")
