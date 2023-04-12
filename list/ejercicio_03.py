lista = []
numero = 0
suma = 0
while numero >= 0:
    numero =int(input("ingrese un numero"))
    if numero > 0:
        lista.append(numero)

for i in lista:
    suma = suma + i
print(suma)