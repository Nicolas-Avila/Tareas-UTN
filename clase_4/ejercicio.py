def conversor_grados_a_fahrenheit(grados):
    '''
    convierte los grados en fahrenheir
    recibe el grado ingresado
    retorna la conversion
    '''
    conversion = grados * 1.8 + 32
    return(conversion)

def calcula_area_circulo(radio_int):
    '''
    calcula el area del circulo
    recibe el radio ingresado
    retorna el area calculada
    '''
    area = 3.14 * radio_int ** 2
    return(area)

def descuento_aplicado(precio_int, descuento_int):
    '''
    calcula el porcentaje de descuento
    recibe el valor original y el valor con descuento
    retorna el porcentaje de descuento 
    '''
    descuento_dado = (descuento_int * 100) / precio_int
    return(descuento_dado)

def promedio_edad(edades : float) -> float:
    '''
    calcula el promedio de las edades
    recibe la lista de la edades
    retorna el promedio calculado
    '''
    acumulador = 0
    for i in edades:
        acumulador += i
    promedio = acumulador / len(edades)
    return(promedio)

def determina_primo(numero_int):
    '''
    determina si es un numero primo
    recibe el numero ingresado
    retorna True si es primo o False si no es primo
    '''
    for i in range(2, numero_int):
        if numero_int % i == 0:
            return (False)
    return (True)

def area_triangulo(base_int : int, altura_int : int) -> float:
    '''
    calcula el area del triangulo
    recibe la altura y la base ingresada
    retorna el area ya calculada
    '''
    area = base_int * altura_int / 2
    return(area)

def par_impar(numero_int):
    '''
    averigua si el numero es par o impar
    recibe un numero
    retorna true si es par y false si es impar
    '''
    if numero_int % 2 == 0:
        return(True)
    else:
        return(False)
    
def elemnto_lista(lista,elemento_int : int) -> int :
    '''
    averigua cuantas veces se repite un numero dado en la lista
    recive la lista y el numero que quiero ver cuanto se repite
    retorna la cantidad de veces que se repite
    '''
    cont = 0
    for i in lista:
        if i == elemento_int:
            cont +=1
    return(cont)

#ejercicio 1
# ingreso_grados=input('ingrese un grado ')
# grados_int = int(ingreso_grados)
# print(conversor_grados_a_fahrenheit(grados_int))    

# ejercicio 2
# ingreso_radio = input('ingrese su radio')
# radio_int = int(ingreso_radio)
# area_muestra = calcula_area_circulo(radio_int)
# print(area_muestra) 

# ejercicio 3
# precio_original = input('ingrese el precio sin descuento')
# precio_int = int(precio_original)
# precio_descuento= input('ingrese el precio on descuento')
# descuento_int = int(precio_descuento)
# descuento_muestra = descuento_aplicado(precio_int, descuento_int)
# print('el descuento es de {0}'.format(descuento_muestra))

# ejercicio 4
# edades = [15,12,18,20]
# promedio_edades = promedio_edad(edades)
# print(promedio_edades)

# ejercicio 5
# numero = input('ingrese un numero')
# numero_int = int(numero)
# numero_primo = determina_primo(numero_int)
# print(numero_primo)

# ejercicio 6
# base = input('ingrese la base')
# base_int = int(base)
# altura = input('ingrese la altura')
# altura_int = int(altura)
# area = area_triangulo(base_int,altura_int)
# print(area)

# ejercicio 7

# ejercicio 8
# numero = input('ingrese un numero')
# numero_int = int(numero)
# print(par_impar(numero_int))

# ejercicio 9
# lista = [8,10,12,8,3,8]
# elemento = input('ingrese el elemento a contar')
# elemento_int = int(elemento)
# print('se repite',elemnto_lista(lista,elemento_int),'veces')

def palbra_larga(lista):
    '''
    averigua que palabra es mas larga de la lista
    recive la lista
    retorna la palabra mas larga
    '''
    palabra_larga = lista [0]
    for i in lista:
        if len(i) > len(palabra_larga):
            palabra_larga = i
    return (palabra_larga)

# ejercicio 10
# lista = ['hola','zoologico','chau']
# print(palbra_larga(lista))

def cantidad_vocales(palabra):
    '''
    averigua la cantidad de vocales que tiene la palabra
    recive la palabra ingresada
    retorna la cantidad de vocales que tiene 
    '''
    cont = 0
    for letra in palabra:
        if letra in 'aeiouAEIOU':
            cont +=1
    return(cont)


# ejercicio 11
# palabra = input('ingrese la palabre')
# print('vocales',cantidad_vocales(palabra))

def igualdad_nombres(nombre_uno,nombre_dos):
    '''
    averigua si se repite mas de una palabra en las 2 listas
    recive la primera y la segunda lista
    retorna las palabras que se repiten
    '''
    nombre = []
    for lista_uno in nombre_uno:
        for lista_dos in nombre_dos:
            if lista_uno == lista_dos:
                nombre.append(lista_uno)
    return(nombre)
# ejercicio 12
# nombre_uno = ['carlos', 'facundo','nico','maria']
# nombre_dos = ['nico','carlos','valentia','pedro']
# print(igualdad_nombres(nombre_uno,nombre_dos))

def diccionario(lista):
    diccionario = []

    for i in lista:
        i = {i : len(i)}
        diccionario.append(i)
    return diccionario

# ejercicio 13
# lista = ['rojo','azul','verde']
# print(diccionario(lista))

def calcula_peliculas_genero(lista_peliculas):
    dic_genero = {}
        
    for pelicula in lista_peliculas:

        if pelicula['genero'] in dic_genero:
            dic_genero[pelicula['genero']] += 1
        else:
            dic_genero[pelicula['genero']] = 1
    
    return dic_genero
    



# ejercicio 15
peliculas = [
    {
    'titulo':'mario',
    'genero':'comedia',
    'director':'alguien'
    },
    {
    'titulo':'sonic',
    'genero':'comedia',
    'director':'alguien'
    },
    {
    'titulo':'simson',
    'genero':'terror',
    'director':'alguien'
    },
    {
    'titulo':'sonic',
    'genero':'comedia',
    'director':'alguien'
    }
]

ave = calcula_peliculas_genero(peliculas)
print(ave)