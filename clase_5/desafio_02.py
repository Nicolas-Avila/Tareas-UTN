from data_stark import lista_personajes

# def stark_normalizar_datos(lista_personajes):
#     for indice in lista_personajes:
#         decimas = indice['altura'].count('.')
#         decimas += 1
#         if 1 < decimas:
#             print('sos bueno')

# stark_normalizar_datos(lista_personajes)

def stark_normalizar_datos_1(heroes: list[dict]) -> None:

    if heroes:
        # Recorro cada diccionario de heroe de la lista
        for heroe in heroes:
            key_list = list(heroe.keys())
            # Recorro las claves que me interesan castear
            for key in key_list:
                if type(heroe[key]) is str:
                    valor_reemplazado: str = heroe[key].replace('.', '')
                    if valor_reemplazado.isnumeric() and type(heroe[key]) is str:
                        if '.' in heroe[key] and heroe[key].count('.') == 1:
                            heroe[key] = float(heroe[key])
                        else:
                            heroe[key] = int(heroe[key])
                        #print(f'El dato {key} fue modificada para el heroe: {heroe["nombre"]}')
    else:
        print('Error La lista esta vacía.')

#1.1
def obtener_nombre(lista_personajes:dict)->str:
    '''
    Obtiene el nombre de la posicion ingresada y lo retorna
    '''
    respuesta = 'nombre: {0}'.format(lista_personajes['nombre'])
    return respuesta

#1.2
def imprimir_dato(dato):
    '''
    Obtiene el dato ingresado y lo impirme por consola
    '''
    print(dato)

#1.3
def stark_imprimir_nombres_heroes(lista_heroes:dict)->None:
    '''
    Recorre el diccionario de heroes e impirme por consola los nombres utilizando la funcion obtener_nombre
    '''
    for heroe in lista_heroes:
        nombre_heroe = obtener_nombre(heroe)
        imprimir_dato(nombre_heroe)

#2
def obtener_nombre_y_dato(dict_heroes:dict,key:str)->None:
    '''
    Obtiene el nombre de la posicion ingresada y el dato ingresado imprimiendolo por consola 
    el nombre lo imprime mediante la funcion obtener_nombre
    '''
    print ('{0} | {1}: {2}'.format(obtener_nombre(dict_heroes),key,dict_heroes[key]))

#3
def stark_imprimir_nombres_alturas(dict_heroe:dict)->None:
    '''
    Valida que la lista no este vacia e impirme nombre y la altura mediante la funicion obterner_nombre_y_dato
    '''
    if len(dict_heroe) > 0:    
        for heroes in dict_heroe:
            obtener_nombre_y_dato(heroes,'altura')
    else:
        print('no hago nada')
#4.1
def calcular_max(dict_heroe:dict,key:str):
    '''
    Accede a cada elemento del diccionario y averigua cual es el mayor del dato ingresado
    '''
    for heroe in range(len(dict_heroe)):
        if heroe == 0 or float(dict_heroe[maximo][key]) < float(dict_heroe[heroe][key]):
            maximo = heroe
    respuesta = 'nombre {0} | {1} {2}'.format(dict_heroe[maximo]['nombre'],key,dict_heroe[maximo][key])
    return respuesta
#4.2
def calcular_min(dict_heroe:dict,key:str):
    '''
    Accede a cada elemento del diccionario y averigua cual es el menor del dato ingresado
    '''
    for heroe in range(len(dict_heroe)):
        if heroe == 0 or float(dict_heroe[minimo][key]) > float(dict_heroe[heroe][key]):
            minimo = heroe
    respuesta = 'nombre: {0} | {1} {2}'.format(dict_heroe[minimo]['nombre'],key,dict_heroe[minimo][key])
    return respuesta
#4.3
def calcular_max_min_dato(dict_heroe:dict,key:str,opcion:str):
    '''
    Averigual el mayor y menor pudiendo elegir entre los dos, mostrandolo con el dato ingresado, utilizando las funciones de calcular_max o calcular_min,
    '''
    if opcion == 'maximo':
        print(calcular_max(dict_heroe,key))
    elif opcion == 'minimo':
        print(calcular_min(dict_heroe,key))
#4.4
def stark_calcular_imprimir_heroe(dict_heroe:dict,key:str,opcion:str):
    '''
    Comprueba que la lista no este vacia, calcula el maximo o el minimo del dato ingresado utilizando la funcion calcular_max_min_dato
    '''
    if len(dict_heroe) > 1:
        print('{0} {1}:'.format(opcion,key,))
        calcular_max_min_dato(dict_heroe,key,opcion)
    else:
        print(-1)
#5.1
def sumar_dato_heroe(dict_heroe:dict,key:str)->str:
    '''
    Comprueba que la lista no este vacia, recorre el diccionario y suma los valores del dato ingresado y retorna el resutado
    '''
    if len(dict_heroe) > 1:
        acumualador = 0
        for heroe in dict_heroe:
            acumualador = acumualador + heroe[key]
    return acumualador
#5.2
def dividir(dividendo:float,divisor:float)->float:
    '''
    Recive 2 numeros y los divide y retorna el resultado
    '''
    if divisor == 0:
        return 0
    else:
        return dividendo/divisor

#5.3
def calcular_promedio(dict_heroe:dict,key:str)->float:
    '''
    Calcula el promedio del dato ingresado utilizando las funciones de dividir y la de sumar_dato_heroe retornando el resultado
    '''
    cont=0
    for i in dict_heroe:
        cont += 1
        return dividir(sumar_dato_heroe(dict_heroe,key),cont)
    
#5.4
def stark_calcular_imprimir_promedio_altura(dict_heroe:dict,key:str ='altura'):
    '''
    Calcula el promedio de la altura utilizando la funcion calcular_promedio y retorna el resultado 
    '''
    return calcular_promedio(dict_heroe,key)

'''
no entendi como pedia el menu y lo hice como se me ocurrio a mi
'''
def ingrese_otra_opcion(opcion):
    '''
    Permite ingresar otra opcion en el match
    '''
    opcion = int(input('ingrese otra opcion: '))
    return opcion
def imprimir_menu():
    '''
    menu de opciones del programa
    '''
    opcion = int(input('ingrese una opcion\n'
                        '1.obtener nombre\n'
                        '2.imprimir dato\n'
                        '3.imprimir nombre de heroes\n'
                        '4.obtener nombre y dato\n'
                        '5.imprimr nombre y alturas\n'
                        '6.calcular maximo\n'
                        '7.calcular minimo\n'
                        '8.calcular maximo y minimo (altura,peso,fuerza)\n'
                        '9.calcula e imprime heroe\n'
                        '10.sumar datos del heroe\n'
                        '11.dividir\n'
                        '12.calcular promedio\n'
                        '13.promedio de altua\n'
                        '14.salir\n'
                        'opcion: '))
    
    while True:
    
        match opcion:

            case 1:
                personaje = int(input('ingrese el numero de personaje que desea ver: '))
                if len(lista_personajes) >= personaje:
                    print(obtener_nombre(lista_personajes[personaje]))
                    opcion = ingrese_otra_opcion(opcion)
                else:
                    print('no existe es personaje')
                    opcion = ingrese_otra_opcion(opcion)
            case 2:
                dato = input('ingrese un dato: ')
                imprimir_dato(dato)
                opcion = ingrese_otra_opcion(opcion)
            case 3:
                stark_imprimir_nombres_heroes(lista_personajes)
                opcion = ingrese_otra_opcion(opcion)
            case 4:
                personaje = int(input('ingrese el numero de personaje que desea ver: '))
                if len(lista_personajes) >= personaje:
                    dato = input('ingrese: nombre, identidad, empresa,'
                                'altura, peso, genero, color_ojos, color_pelo, fuerza, inteligencia')
                    obtener_nombre_y_dato(lista_personajes[personaje],dato)
                    opcion = ingrese_otra_opcion(opcion)
                else:
                    print('no existe es personaje')
                    opcion = ingrese_otra_opcion(opcion)
            case 5:
                stark_imprimir_nombres_alturas(lista_personajes)
                opcion = ingrese_otra_opcion(opcion)
            case 6:
                dato= input('ingrese el dato a averiuar altura, peso, fuerza: ')
                print(calcular_max(lista_personajes,dato))
                opcion = ingrese_otra_opcion(opcion)
            case 7:
                dato= input('ingrese el dato a averiuar altura, peso, fuerza: ')
                print( calcular_min(lista_personajes,dato))
                opcion = ingrese_otra_opcion(opcion)
            case 8:
                dato= input('ingrese el dato a averiuar altura, peso, fuerza: ')
                averiguar = input('desea averiguar el minimo o el maximo: ')
                calcular_max_min_dato(lista_personajes,dato,averiguar)
                opcion = ingrese_otra_opcion(opcion)
            case 9:
                dato= input('ingrese el dato a averiuar altura, peso, fuerza: ' )
                averiguar = input('desea averiguar el minimo o el maximo: ')
                stark_calcular_imprimir_heroe(lista_personajes,dato,averiguar)
                opcion = ingrese_otra_opcion(opcion)
            case 10:
                dato= input('ingrese el dato a sumar altura, peso, fuerza: ')
                print(sumar_dato_heroe(lista_personajes,dato))
                opcion = ingrese_otra_opcion(opcion)
            case 11:
                dividendo = int(input ('ingrese el dividendo: '))
                divisor = int(input('ingrese el divisor: '))
                print(dividir(dividendo,divisor))
                opcion = ingrese_otra_opcion(opcion)
            case 12:
                dato = input('ingrese el dato a averiuar altura, peso, fuerza: ')
                print(calcular_promedio(lista_personajes,dato))
                opcion = ingrese_otra_opcion(opcion)
            case 13:
                print(stark_calcular_imprimir_promedio_altura(lista_personajes))
                opcion = ingrese_otra_opcion(opcion)
            case 14:
                break
            case _:
                print('esa opcion no se encuentra en el menu')
                opcion = ingrese_otra_opcion(opcion)

stark_normalizar_datos_1(lista_personajes)
print(imprimir_menu())