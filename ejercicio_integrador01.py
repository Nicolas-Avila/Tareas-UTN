numeroIdentificacion = [12,45,67]
nombre = ['tomas','nico','ave']
edad = [18,150,9]
membresia = ['anual','mensual','anual']

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
        ingresoIdentificacion = input('ingrese el numero de identificacion')
        ingresoNombre = input('ingrese su nombre')
        ingresoEdad = input('ingrese su edad')
        ingresoMembresia = input('ingrese su membresia (anual o mensual)')

        numeroIdentificacion.append(ingresoIdentificacion)
        nombre.append(ingresoNombre)
        edad.append(ingresoEdad)
        membresia.append(ingresoMembresia)
       
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        for indice in range(len(numeroIdentificacion)):
            if indice < len(numeroIdentificacion) :
                print('Identificacion:{0} nombre:{1} edad:{2} membresia:{3} '.format(numeroIdentificacion[indice], nombre[indice], edad[indice], membresia[indice]))
       
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        buscarMiembro = int(input('ingrese el numero de la membresia a cambiar'))
        nuevaMembresia = input('ingrese la nueva membresia (anuel o mensual)')

        for indice in range(len(membresia)):
            if numeroIdentificacion[indice] == buscarMiembro:
                membresia[indice] = nuevaMembresia
                print('cambiado con exito')
                print('Identificacion:{0} nombre:{1} edad:{2} membresia:{3} '.format(numeroIdentificacion[indice], nombre[indice], edad[indice], membresia[indice]))
            

    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        buscarMiembro =input('ingrese el numero de la membresia a buscar: ')
        buscarMiembro = int(buscarMiembro)
        for indice in range(len(numeroIdentificacion)):
            if numeroIdentificacion[indice] == buscarMiembro:
                print('Identificacion:{0} nombre:{1} edad:{2} membresia:{3} '.format(numeroIdentificacion[indice], nombre[indice], edad[indice], membresia[indice]))
                break
            else:
                print('ese miembro no existe')
                break


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        promedio = 0
        for indice in edad:
            promedio = promedio + indice  
        resultado = promedio / len(edad)
        print(resultado) 

    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        edadMayor = False
        edadMenor = False

        mayor = edad[0]  
        menor = edad[0]
        for indice in edad:
            
            if indice > mayor:
                mayor = indice
                edadMayor = True
        
            if indice < menor:
                menor = indice
                edadMenor = True

        if edadMayor == True:
            print('la edad mayor es de: {0} años '.format(mayor))
            
        if edadMenor == True:
            print('la edad menor es de: {0} años '.format(menor))
                
    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")
