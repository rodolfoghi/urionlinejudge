valor = int(input())

cedulas = [100, 50, 20, 10, 5, 2 , 1]

print(valor)

for cedula in cedulas:
  qt_cedulas = int(valor / cedula)
  print("{} nota(s) de R$ {},00".format(qt_cedulas, cedula))
  valor -= qt_cedulas * cedula