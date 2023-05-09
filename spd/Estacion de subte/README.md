

## Integrantes 
- Daniel Nicolas Avila  



## Proyecto: Contador binario.
![Tinkercad](./img/ContadorBinario.png)


## Descripción
Deberá recorrer las estaciones comenzando por constitución y mostrará en el display 7 segmentos cuantas estaciones faltan para llegar a moreno


## Función principal
Un sistema que permite al usuario saber a qué estación de subte está llegando, aparte  el sistema muestra las estaciones que faltan hasta llegar a destino.

B0, B1, B2, B3 son #define que utilizamos para agregar los leds, asociandolo a pines de la placa arduino.

(Breve explicación de la función)

~~~ C (lenguaje en el que esta escrito)
void EncenderBinario(int estado3, int estado2,int estado1,int estado0)
{
  digitalWrite(B3,estado3);
  digitalWrite(B2,estado2);
  digitalWrite(B1,estado1);
  digitalWrite(B0,estado0);
}
~~~

## :robot: Link al proyecto
- [proyecto](https://www.tinkercad.com/things/98kFuGyBpyC)









