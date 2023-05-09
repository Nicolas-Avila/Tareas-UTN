

## Integrantes 
- Daniel Nicolas Avila  



## Proyecto: Contador binario.
![Tinkercad](./img/circuito.png)


## Descripción
Deberá recorrer las estaciones comenzando por constitución y mostrará en el display 7 segmentos cuantas estaciones faltan para llegar a moreno


## Función principal
Un sistema que permite al usuario saber a qué estación de subte está llegando, aparte  el sistema muestra las estaciones que faltan hasta llegar a destino.

(Breve explicación de la función)

~~~ C (lenguaje en el que esta escrito)
void display_nro(int cont) {
  if (cont == 1) {
    digitalWrite(displayA, HIGH);
    digitalWrite(displayB, HIGH);
    digitalWrite(displayC, HIGH);
    digitalWrite(displayD, HIGH);
    digitalWrite(displayE, HIGH);
    digitalWrite(displayF, HIGH);
    delay(2000);
    display_apagado();
    cont++;
  }
~~~

## :robot: Link al proyecto
- [proyecto](https://www.tinkercad.com/things/98kFuGyBpyC)









