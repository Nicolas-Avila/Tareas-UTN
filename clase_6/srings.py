def mayuscula_minuscula(ingreso,mayus):
    if mayus == True:
        mayuscula = ingreso.upper()
        return mayuscula
    else:
        minuscula = ingreso.lower()
        return minuscula

def union_string(ingreso,otro_ingreso):
    union = (ingreso,otro_ingreso)
    return" ".join(union)

def cantidad_caracter(ingreso):
    return len(ingreso)

def caracter_especifico(ingreso,caracter):
    return caracter,ingreso.count(caracter)

#realizar el 6

def sin_espacios(ingreso):
    return ingreso.replace(" ","")

def diccionario_sin_espacios(ingreso,otro_ingreso):
    diccionario = {
        "nombre":ingreso.split(),
        'apellido':otro_ingreso.split()
    }
    return diccionario

def unir_cadena(lista):
    agrega = '\n'
    agrega = agrega.join(lista)
    return agrega

def crea_email(nombre,apellido):
    email = '{0}_{1}.{2}@utn-fra.com.ar'.format(nombre[0],nombre,apellido)
    return email

def agrega_coma_y(lista):
    return", ".join(lista[:-1]) + " y " + lista[-1]

def numero_oculato(tarjeta):
    return '**** **** **** {0}'.format(tarjeta[-5:-1])

def sacar_email(email):
    usuario = email.split('@')
    return usuario[0]

def dominio(email):
    nombre_dominio = email.split('.')
    return nombre_dominio[1]
menu = input('ingrese la opcion')



match menu:

    case '1':
        ingreso = input('ingrese una palabra\n')
        print(mayuscula_minuscula(ingreso,True))
    case '2':
        ingreso = input('ingrese una palabra\n') 
        print(mayuscula_minuscula(ingreso,False))
    case '3':
        ingreso = input('ingrese una palabra\n')
        otro_ingreso = input('ingrese otra palabra:\n')
        print(union_string(ingreso,otro_ingreso))
    case '4':
        ingreso = input('ingrese una palabra\n')
        print(cantidad_caracter(ingreso))
    case '5':
        ingreso = input('ingrese una palabra\n')
        caracter = input('ingrese el caracter para averiguar\n')
        print(caracter_especifico(ingreso,caracter))
    case '6':
        pass
    case '7':
        ingreso = input('ingrese una palabra\n')
        print(sin_espacios(ingreso))
    case '8':
        ingreso = input('ingrese una palabra\n')
        otro_ingreso = input('ingrese otra palabra:\n')
        print(diccionario_sin_espacios(ingreso,otro_ingreso))
    case '9':
        lista = ['tomas','nico','hola']
        print(unir_cadena(lista))
    case '10':
        nombre = input('ingrese nombre')
        apellido = input('ingrese apellido')
        print(crea_email(nombre,apellido))
    case '11':
        lista = ['tomate', 'manzana','peras']
        print(agrega_coma_y(lista))
    case '12':
        tarjeta = input('ingrese su tarjeta')
        print(numero_oculato(tarjeta))
    case '13':
        email = input('ingrese un email')
        print(sacar_email(email))
    case '14':
        email = input('ingrese su email')
        print(dominio(email))
    



#1
# print('en mayuscula {0}'.format(ingreso.upper()))

# #2
# print('en minuscula {0}\n'.format(ingreso.lower()))

# #3
# otro_ingreso = input('ingrese otra palabra:\n')
# union = (ingreso,otro_ingreso)
# print(" ".join(union))

# #4
# print('la palabra {1} tiene {0} caracteres\n'.format(len(ingreso),ingreso))

# #5
# caracter = input('ingrese el caracter para averiuar\n')
# print('el caracter {0} aparece {1} veces en la palabra {2}\n'.format(caracter,ingreso.count(caracter),ingreso))

# #6
# lista_caracter = [ingreso.count(caracter)]

# print(lista_caracter)