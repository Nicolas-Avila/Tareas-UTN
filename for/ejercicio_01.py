numero = [1,2,3,4,19,5,6]
numero_mayor = numero[0]

for num in numero:
    if num > numero_mayor:
        numero_mayor = num

print("el numero mayor es {0}".format(numero_mayor))
