#Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima "El número ingresado es positivo" si el número es mayor que cero, o "El número ingresado es cero o negativo" si el número es menor o igual a cero.

numero_string = input("ingrese numero")
numero = int(numero_string)

if (numero > 0):
    print("el numero ingresado es positivo")
else:
    print("el numero es cero o negativo")    