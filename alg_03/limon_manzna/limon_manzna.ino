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

//Calculo de Limon - Naranja
float x1 = 0;
float x2 = 0;
float x3 = 0;

void setup() {
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

void loop() {
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

  calculo();
  delay(2000);

}

float relu(float dato){
  if(dato > 0){
    return dato;
  }else{
    return 0;
  }
}

float sigmoid(float dato){
  return (1/(1 + exp(dato * -1)));
}

void calculo(){
  x1 = frecuenciaRojo;
  x2 = frecuenciaVerde;
  x3 = frecuenciaAzul;
  float n1 = relu( (x1 * (-0.5471446)) + (x2 * (-0.8426175)) + (x3 * ( 0.1457299)) + (0) );
  float n2 = relu( (x1 * (1.1483318)) + (x2 * (-0.83082044)) + (x3 * (-0.04601754)) + (-0.07825806) );
  float n3 = sigmoid( (n1 * (-0.75196415)) + (n2 * (0.03152713)) + (-6.3203387) );
  //Serial.print(n1);
  //erial.print(n2);
  //Serial.print(n3);
  if(round(n3) == 1){
    Serial.println("Limón");
  }else{
    Serial.println("Naranja");
  }
}

