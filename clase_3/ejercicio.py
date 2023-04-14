from data_stark import lista_personajes

def nombre_superheroes():
    for nombre in lista_personajes:
        print('el nombre del superheroe es: {0}'.format(nombre['nombre']))
    
def nombre_altura_superheroes():
    for nombre in lista_personajes:
        print('el nombre del superheroe es: {0} y su altura es: {1}'.format(nombre['nombre'],nombre['altura']))

def superheroe_alto():
    for indice in range(len(lista_personajes)):

        if indice == 0 or float(lista_personajes[mas_alto]['altura']) < float(lista_personajes[indice]['altura']):
            mas_alto = indice
    print('el superheroe mas alto es: {0} con {1} metros'.format(lista_personajes[mas_alto]['nombre'],lista_personajes[mas_alto]['altura']))

def superheroe_bajo():
    for indice in range(len(lista_personajes)):

        if indice == 0 or float(lista_personajes[mas_bajo]['altura']) > float(lista_personajes[indice]['altura']):
            mas_bajo = indice
    print('el superheroe mas bajo es: {0} con {1} metros'.format(lista_personajes[mas_bajo]['nombre'],lista_personajes[mas_bajo]['altura']))

def altura_promedio():
    acumulador = 0
    for altura in lista_personajes:
        acumulador += float(altura['altura'])
    
    print('El promedio de altura es de {0}'.format(acumulador/len(lista_personajes)))

def mas_menos_pesado():
    for indice in range(len(lista_personajes)):

        if indice == 0 or float(lista_personajes[mas_pesado]['peso']) < float(lista_personajes[indice]['peso']):
            mas_pesado = indice
    print('el superheroe mas pesado es: {0} con {1} kilos \n'.format(lista_personajes[mas_pesado]['nombre'],lista_personajes[mas_pesado]['peso']))

    for indice in range(len(lista_personajes)):

        if indice == 0 or float(lista_personajes[menos_pesado]['peso']) > float(lista_personajes[indice]['peso']):
            menos_pesado = indice
    print('el superheroe menos pesado es: {0} con {1} kilos'.format(lista_personajes[menos_pesado]['nombre'],lista_personajes[menos_pesado]['peso']))

while True:
    print ('\n1. Nombre de los superheroes\n2. Nombre y su altura'
                    '\n3. Superheroe mas alto\n4. Superheroe mas bajo\n5. Altura promedio\n6. Identidad del superheroe mas bajo y alto'
                    '\n7. Superheroe mas y menos pesado\n8. Salir')
    respuesta = input('')
    match respuesta:

        case '1':
            nombre_superheroes()

        case '2':
            nombre_altura_superheroes() 

        case '3':
            superheroe_alto()

        case '4':
            superheroe_bajo()

        case '5':
            altura_promedio()

        case '6':
            superheroe_alto()
            superheroe_bajo()

        case '7':
            mas_menos_pesado()

        case '8':
            break

        case _:
            print('esa opcion no exixste')