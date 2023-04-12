lista = []

while True:
    palabra = input("escriba")
    if palabra[0] == "z":
        break
    else:
        lista.append(palabra)
        print(palabra[0])
