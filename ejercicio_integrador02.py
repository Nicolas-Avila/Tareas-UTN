
lista_gimnasio = []

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        miembro_nuevo = {}
        miembro_nuevo['numero_identificador'] = input('ingrese el codigo identificador ')
        miembro_nuevo['nombre'] = input('ingrese su nombre ')
        miembro_nuevo['membresia'] = input('ingrese su membresia (anual o mensual) ')
        miembro_nuevo['edad'] = input('ingrese su edad ')

        lista_gimnasio.append(miembro_nuevo)
        
    
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        for indice in lista_gimnasio:
            print('el numero identificador es {0} su nombre {1} su membresia es {2} y su edad es {3}'
                                .format(indice['numero_identificador'],
                                        indice['nombre'],
                                        indice['membresia'],
                                        indice['edad']))
        #print(miembro_nuevo['numero_identificador','nombre','membresia','edad'])
    
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        buscar_identificador = int(input('ingrese el codigo de identificacion'))
        membresia_nueva = ('ingrese su nueva membresia (anual o mensual)')

        for indice in lista_gimnasio:
            if indice['numero_identificador'] == buscar_identificador:
                indice['membresia'] = membresia_nueva
    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        pass


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        pass


    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        pass


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")