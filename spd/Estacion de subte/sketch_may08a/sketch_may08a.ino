//led estaciones
#define constitucion 13
#define sanJuan 12
#define independencia 11
#define moreno 10
//interruptor
int estadoInterruptor = 0;
#define interruptor 9
//display
#define displayG 8
#define displayF 7
#define displayA 6
#define displayB 5
#define displayE A3
#define displayD A2
#define displayC A1
//sonido
int tono = 1000;
#define piezo A0


void setup()
{
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(constitucion, OUTPUT);
  pinMode(sanJuan, OUTPUT);
  pinMode(independencia, OUTPUT);
  pinMode(moreno, OUTPUT);


  pinMode(interruptor, INPUT);

  pinMode(displayG, OUTPUT);
  pinMode(displayF, OUTPUT);
  pinMode(displayA, OUTPUT);
  pinMode(displayB, OUTPUT);
  pinMode(displayE, OUTPUT);
  pinMode(displayD, OUTPUT);
  pinMode(displayC, OUTPUT);

  pinMode(piezo, OUTPUT);


}

int cont = 1;
void loop()
{
  estadoInterruptor = digitalRead(interruptor);

  if (estadoInterruptor == HIGH) {

    estacion(cont);

    cont++;

  }


}

void estacion(int cont) {

  if (cont == 1) {
    sonido();
    digitalWrite(constitucion, HIGH);
    display_nro(cont);

    digitalWrite(constitucion, LOW);
    cont++;
  }
  else if (cont == 2) {
    sonido();
    digitalWrite(sanJuan, HIGH);
    display_nro(cont);

    digitalWrite(sanJuan, LOW);
    cont++;
  }
  else if (cont == 3) {
    sonido();
    digitalWrite(independencia, HIGH);
    display_nro(cont);

    digitalWrite(independencia, LOW);
    cont++;
  }
  else if (cont == 4) {
    sonido();
    digitalWrite(moreno, HIGH);
    display_nro(cont);
    digitalWrite(moreno, LOW);
    cont++;
  }
}


void display_apagado() {
  digitalWrite(displayA, LOW);
  digitalWrite(displayB, LOW);
  digitalWrite(displayC, LOW);
  digitalWrite(displayD, LOW);
  digitalWrite(displayE, LOW);
  digitalWrite(displayF, LOW);
  digitalWrite(displayG, LOW);
}

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
  else if (cont == 2) {
    digitalWrite(displayB, HIGH);
    digitalWrite(displayC, HIGH);
    delay(2000);
    display_apagado();
    cont++;
  }
  else if (cont == 3) {
    digitalWrite(displayA, HIGH);
    digitalWrite(displayB, HIGH);
    digitalWrite(displayG, HIGH);
    digitalWrite(displayD, HIGH);
    digitalWrite(displayE, HIGH);
    delay(2000);
    display_apagado();
    cont++;
  }
  else if (cont == 4) {
    digitalWrite(displayA, HIGH);
    digitalWrite(displayB, HIGH);
    digitalWrite(displayC, HIGH);
    digitalWrite(displayG, HIGH);
    digitalWrite(displayD, HIGH);
    delay(2000);
    display_apagado();
    cont = 1;
  }
}

void sonido() {
  tone(piezo, tono);
  delay(1000);
  noTone(piezo);
}
