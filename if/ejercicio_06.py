nombre = input("ingrese su nombre")
edad = int(input("ingrese su edad"))

if edad >= 18 and edad < 65:
    print("puede votar")
else:
    print("no puede votar")