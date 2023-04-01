lista = [20,40,4,5]
lista_menor = lista[0]
for i in lista:
    if lista_menor > i:
        lista_menor = i

print("el numero menor es {0}".format(lista_menor))
