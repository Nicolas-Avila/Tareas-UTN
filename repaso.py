#respuesta = "s"

#while(respuesta == "s"):
#   respuesta = input("continuar s o n ")

#numero = input("ingrese numero")
#cont = 1
#numero_int=int(numero)

#while(cont <= numero_int):
#    print(cont)
#    cont += 1

# #for
# lista_numero = [1,2,3,4,5]
# # # lista_numero = list(range(5))

# for numero in lista_numero:

#     if(numero == 3):
#         continue #se saltea el numero 3 
#         break #corta l amuestra cuedo llega al 3
#     print(numero, end=" ")

# while(True):
#     numero_texto = int(input("numero"))
#     if(numero_texto == 12):
#         break

#"match" seria el swicht de python

texto = input()

match texto:
    case "hola":
        print("ey {0} - {1}".format(texto, """otra variable""") )
    case "chau":
        pass
    case _:
        print("tonto")