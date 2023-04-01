palabras = ["hola", "larga", "cuerdas"]
palabra_larga = palabras[0]

for palabra_mas_larga in palabras:
    if len(palabra_mas_larga) > len(palabra_larga):
        palabra_larga = palabra_mas_larga

print("la palabra mas larga es {0}".format(palabra_larga))
