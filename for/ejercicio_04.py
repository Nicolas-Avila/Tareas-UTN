numero = input ("ingrese numero")
numero_int = int(numero)
suma = 0
for i in range(1,numero_int+1,2):
    suma = suma + i
print("la suma de los numero impares de de{0}".format(suma))