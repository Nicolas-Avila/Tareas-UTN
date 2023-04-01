#terminar
numero = input("ingrese un numero entero positivo")
numero_int = int(numero)

if numero_int > 1:
    for primo in range(2, numero_int):
        if (numero_int % primo) == 0:
            print("no es un numero primo")

            break

        else:
            print("es un numero primo")
            break
