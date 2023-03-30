#Escribir un programa que le pida al usuario que ingrese su edad, y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18, o "Eres menor de edad" si la edad es menor a 18.

numero= int(input("ingrese la edad"))

if (numero >= 18):
    print("es mayor de edad")
else:
    print("es menor de edad")    