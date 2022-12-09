//Sensor a Arduino
#define S0 8
#define S1 9
#define S2 12
#define S3 11
#define salidaSensor 10

// Para guardar las frecuencias de los fotodiodos
int frecuenciaRojo = 0;
int frecuenciaVerde = 0;
int frecuenciaAzul = 0;

void setup(){
  // Definiendo las Salidas
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);

  // Definiendo salidaSensor como entrada
  pinMode(salidaSensor, INPUT);

  // Definiendo la escala de frecuencia a 20%
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);

  // Iniciar la comunicacion serie 
  Serial.begin(9600);
}

void loop(){
// Definiendo la lectura de los fotodiodos con filtro rojo
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);

  // Leyendo la frecuencia de salida del sensor
  frecuenciaRojo = pulseIn(salidaSensor, LOW);
  delay(200);

  // Definiendo la lectura de los fotodiodos con filtro verde
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);

  // Leyendo la frecuencia de salida del sensor
  frecuenciaVerde = pulseIn(salidaSensor, HIGH);
  delay(200);
 
  // Definiendo la lectura de los fotodiodos con filtro azul
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);

  // Leyendo la frecuencia de salida del sensor
  frecuenciaAzul = pulseIn(salidaSensor, LOW);
  delay(200);

  //Imprimimos los valores obtenidos
  //Serial.print("R: ");
  Serial.print(frecuenciaRojo);
  Serial.print(" ");

  //Serial.print("G: ");
  Serial.print(frecuenciaVerde);
  Serial.print(" ");

  //Serial.print("B: ");
  Serial.print(frecuenciaAzul);
  Serial.println(" 1");


}