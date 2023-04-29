from data_stark import lista_personajes

def nombre_m_f(genero : int) -> None:
    for nombre in lista_personajes:
        if nombre['genero'] == genero:
            print('el nombre del superheroe es: {0}'.format(nombre['nombre']))

def heroe_altura(genero : int ,altura: int) -> None:
    if altura == 'alto':
        heroe_aux = {}
        for heroe in lista_personajes:
            if not heroe_aux and heroe['genero'] == genero:
                heroe_aux = heroe
            
            if heroe_aux and heroe['genero'] == genero and float(heroe_aux['altura']) < float(heroe['altura']):
                heroe_aux = heroe
        print('el nombre es {0} y la altura es {1}'.format(heroe_aux['nombre'],heroe_aux['altura']))
    else:
        heroe_aux = {}
        for heroe in lista_personajes:
            if not heroe_aux and heroe['genero'] == genero:
                heroe_aux = heroe
            
            if heroe_aux and heroe['genero'] == genero and float(heroe_aux['altura']) > float(heroe['altura']):
                heroe_aux = heroe
        print('el nombre es {0} y la altura es {1}'.format(heroe_aux['nombre'],heroe_aux['altura']))

def altura_promedio(genero : int) -> None:
    acumulador = 0
    for indice in lista_personajes:
        if indice['genero'] == genero:
            acumulador += float(indice['altura'])
    print('El promedio de altura es de {0}'.format(acumulador/len(lista_personajes)))


def contar_colores(colores : str):
    dic_contador_color = {}
    for personaje in lista_personajes:
        texto_colores = personaje[colores]
        texto_nombre = personaje['nombre']

        if texto_colores in dic_contador_color:
            auxiliar_lista = []
            auxiliar_lista = dic_contador_color[texto_colores]
            auxiliar_lista.append(texto_nombre)
        else:
            auxiliar_lista = []
            auxiliar_lista.append(texto_nombre)
            dic_contador_color[texto_colores] = auxiliar_lista

    return dic_contador_color


def contar_inteligencias():
    dic_contador_inteligencia = {}
    for personaje in lista_personajes:
        texto_inteligencia = personaje["inteligencia"]
        texto_nombre = personaje['nombre']

        if texto_inteligencia in dic_contador_inteligencia:
            auxiliar_lista = []
            auxiliar_lista = dic_contador_inteligencia[texto_inteligencia]
            auxiliar_lista.append(texto_nombre)

        elif texto_inteligencia == "":
            texto_inteligencia = "No tiene"
            auxiliar_lista = []
            auxiliar_lista.append(texto_nombre)
            dic_contador_inteligencia[texto_inteligencia] = auxiliar_lista

        else:
            auxiliar_lista = []
            auxiliar_lista.append(texto_nombre)
            dic_contador_inteligencia[texto_inteligencia] = auxiliar_lista

    return dic_contador_inteligencia


while True:
    respuesta = input('')
    match respuesta:
        
        case '1':
            nombre_m_f("M")

        case '2':
            nombre_m_f('F')

        case '3':
            heroe_altura('M','alto')
        case '4':
            heroe_altura('F','alto')

        case '5':
            heroe_altura('M','bajo')
        case '6':
            heroe_altura('F','bajo')

        case '7':
            altura_promedio('M')
        case'8':
            altura_promedio('F')

        case'9':
            colores = contar_colores("color_ojos")
            for color in colores:
                print("------------------")
                print(color)
                print(len(colores[color]))
                print(colores[color])

        case'10':
            colores = contar_colores("color_pelo")
            for color in colores:
                print("------------------")
                print(color)
                print(len(colores[color]))
                print(colores[color])

        case'11':
            inteligencia = contar_inteligencias()
            for inteligencia_heroe in inteligencia:
                print("------------------")
                print(inteligencia_heroe)
                print(len(inteligencia[inteligencia_heroe]))
                print(inteligencia[inteligencia_heroe])
