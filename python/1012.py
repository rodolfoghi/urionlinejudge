'''
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159) 
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.

Input
The input file contains three double values with one digit after the decimal point.

Output
The output file must contain 5 lines of data. Each line corresponds to one of the areas described above, always with a corresponding message (in Portuguese) and one space between the two points and the value. The value calculated must be presented with 3 digits after the decimal point.
'''
# -*- coding: utf-8 -*-

pi_value = 3.14159

values = input().split(" ")
a = float(values[0])
b = float(values[1])
c = float(values[2])

triangulo = a * c / 2
print("TRIANGULO: %.3f" % triangulo)

circulo = pi_value * (c ** 2)
print("CIRCULO: %.3f" % circulo)

trapezio = ((a + b) * c) / 2
print("TRAPEZIO: %.3f" % trapezio)

quadrado = b ** 2
print("QUADRADO: %.3f" % quadrado)

retangulo = a * b
print("RETANGULO: %.3f" % retangulo)
