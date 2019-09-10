# -*- coding: utf-8 -*-

tipo1 = input()
tipo2 = input()
tipo3 = input()

bichos = []
bichos.append(["aguia", "carnivoro", "ave", "vertebrado"])
bichos.append(["pomba", "onivoro", "ave", "vertebrado"])
bichos.append(["homem", "onivoro", "mamifero", "vertebrado"])
bichos.append(["vaca", "herbivoro", "mamifero", "vertebrado"])
bichos.append(["pulga", "hematofago", "inseto", "invertebrado"])
bichos.append(["lagarta", "herbivoro", "inseto", "invertebrado"])
bichos.append(["sanguessuga", "hematofago", "anelideo", "invertebrado"])
bichos.append(["minhoca", "onivoro", "anelideo", "invertebrado"])

for bicho in bichos:
    if tipo1 == bicho[3] and tipo2 == bicho[2] and tipo3 == bicho[1]:
        print(bicho[0])
