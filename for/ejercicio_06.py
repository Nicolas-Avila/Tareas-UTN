lista =["hola","chau"]
vocales = ["a","e","i","o","u"]
cont = 0
for palabra in lista:
    for i in palabra:
        if i.lower() in vocales:
            cont += 1

print("tiene un total de {0} vocales".format(cont))
print(cont)