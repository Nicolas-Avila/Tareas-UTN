lista = [5,50,80,120,21]
#80 120 
promedio=0
suma=0
for i in lista:
    promedio = (promedio + i)

promedio = promedio / 5
#print(promedio)

for mayor in lista:
    if promedio < mayor:
        print(mayor)
        suma = suma + mayor
print(suma)