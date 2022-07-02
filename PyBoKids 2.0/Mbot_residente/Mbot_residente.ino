#include "MeMCore.h"
// Onboard LED port/slot definitions
const int PORT = 7;
const int SLOT = 2;
// Declare the objects
MeUltrasonicSensor ultraSensor(PORT_3);
MeLineFollower SigueLineas(PORT_1); 
MeRGBLed led(PORT, SLOT);
MeDCMotor motorIzdo(M1);
MeDCMotor motorDcho(M2);
MeBuzzer buzzer;
MeLightSensor lightSensor(PORT_6);



void Send_DistanceMessage () {
  int DistanceValue = ultraSensor.distanceCm();
  String DistanceValueString = String(DistanceValue);
  String DistanceMessage = "0;" + DistanceValueString; 
  Serial.println(DistanceMessage);
}

void Send_LineFollowerMessage () {
  int LineFollowerValue = SigueLineas.readSensors();
  String LineFollowerString = String(LineFollowerValue);
  String LineFollowerMessage = "1;" + LineFollowerString; 
  Serial.println(LineFollowerMessage);
}

void Send_LigthSensorMessage () {
  int LigthValue = lightSensor.read();
  String LigthString = String(LigthValue);
  String LigthMessage = "2;" + LigthString; 
  Serial.println(LigthMessage);
}

void read_LedsMessage (String mensaje) {
  int IndexLeds = mensaje.indexOf(';');
  String leds = mensaje.substring(0, IndexLeds);
  int IndexRed = mensaje.indexOf(';', IndexLeds+1);   //finds location of second ,
  String red = mensaje.substring(IndexLeds+1, IndexRed+1);
  int IndexGreen = mensaje.indexOf(';', IndexRed+1);   //finds location of third ,
  String green = mensaje.substring(IndexRed+1, IndexGreen+1);
  String blue = mensaje.substring(IndexGreen+1,-1); //captures remain part of data after last ,
  int ledsInt = leds.toInt();
  int redInt = red.toInt();
  int greenInt = green.toInt();
  int blueInt = blue.toInt();
  led.setColor(ledsInt, redInt, greenInt, blueInt);
  led.show();
}

void read_MotorsMessage (String mensaje) {
  int IndexIzdo = mensaje.indexOf(';');
  String izdo = mensaje.substring(0, IndexIzdo);
  String dcho = mensaje.substring(IndexIzdo+1,-1); //captures remain part of data after last ';'

  int izdoInt = izdo.toInt();
  int dchoInt = dcho.toInt();
  motorIzdo.run(-izdoInt); //el motor izdo va del revés
  motorDcho.run(dchoInt);
}

void playBuzzer (int note, int seconds)
{
  int duration = 1000 * seconds; // la duracion de la funcion es en milisegundos, por lo que hay que multiplicar
  int pauseBetweenNotes = duration * 1.30; // note's duration + 30% seems to work well
  buzzer.tone(note,duration);
  delay(pauseBetweenNotes);
  // stop the tone playing:
  buzzer.noTone();
}
void read_BuzzerMessage (String mensaje) {
  int IndexNote = mensaje.indexOf(';');
    String note = mensaje.substring(0, IndexNote);  
    String duration = mensaje.substring(IndexNote+1,-1); //captures remain part of data after last ;
    int NoteInt = note.toInt() ;
    int DurationInt = duration.toInt();

    int durationValue = 1000 * DurationInt; // la duracion de la funcion es en milisegundos, por lo que hay que multiplicar    
    int pauseBetweenNotes = durationValue * 1.30; // note's duration + 30% seems to work well
    buzzer.tone(NoteInt,durationValue);
    delay(pauseBetweenNotes);
    buzzer.noTone();
}

void Stop_Motors () {
  motorIzdo.stop();
  motorDcho.stop();
}

void Stop_Leds () {
  led.setColor(0, 0, 0, 0);
  led.show();
}

void Stop_Buzzer () {
  buzzer.noTone();
}

//// programa principal

void setup() {
  // put your setup code here, to run once:
  //iniciamos el puerto serie
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  Send_DistanceMessage();
  Send_LineFollowerMessage(); 
  Send_LigthSensorMessage();

  if (Serial.available()>0){
    String mensaje = Serial.readString();
        if (mensaje.equalsIgnoreCase("quit")) {
        Stop_Motors();
        Stop_Leds();
        Stop_Buzzer();
        exit(0);
    }
    int indexActuator = mensaje.indexOf(';');
    String Actuator = mensaje.substring(0,indexActuator);
    String mensajeActuador = mensaje.substring(indexActuator+1);
    if (Actuator == "0") {
      read_LedsMessage(mensajeActuador);
    } else if (Actuator == "1") {
      read_MotorsMessage(mensajeActuador);
    } else if (Actuator == "2") {
      read_BuzzerMessage(mensajeActuador);
    }
  }
}
