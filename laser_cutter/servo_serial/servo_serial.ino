#include <Servo.h>

Servo servoA;
int servoAPin = 9;
int servoBPin = 10;
Servo servoB;

void setup() {
  // put your setup code here, to run once:

  servoA.attach(servoAPin);
  servoB.attach(servoBPin);
  Serial.begin(9600);
  delay(500);
  Serial.write("ready");
}



void loop() {

  static int v = 0;

  if ( Serial.available()) {
    char ch = Serial.read();

    switch(ch) {
      case '0'...'9':
      //Pretty goddamn clever right here. Not mine.
        v = v * 10 + ch - '0';
        break;
      case 'a':
        servoA.write(v);
        Serial.write(v);
        v = 0;
        break;
      case 'b':
        servoB.write(v);
        Serial.write(v);
        v = 0;
        break;
    }
  }
}
