#include <Servo.h>
//#include <SoftwareSerial.h>
#define RATIO 425/(PI/4)
#define BRATIO -400/(PI/4)
#define CRATIO -550/(PI/4)
#define AZERO 1606
//#define AZERO 2020
#define BZERO 1645
#define CZERO 2560
#define D 200.

Servo servoA, servoB, servoC;  // create servo object to control a servo
String v = "";
int sign = 1;
float a = 0.;
float b = 0.;
float c = 0.;
float x_temp;
float y_temp;
float angles[3] = {0.,0.,0.};

//SoftwareSerial ser(2,3);

void setup()
{
  servoA.attach(9);
  servoB.attach(10);
  servoC.attach(11);  // attaches the servo on pin 9 to the servo object
  move(angles);
  Serial.begin(19200);
  //ser.begin(9600);
}


void loop() {
  // put your main code here, to run repeatedly:
  
  
  if (Serial.available()) {
    char ch = Serial.read();
    //Serial.write(ch);
    
    switch(ch) {
      case ';':
        getAngles(v,angles);
        for(int i = 0; i<3 ; i++){
        Serial.println(angles[i]);
        }
        move(angles);
        resetV();
      break;
      default:
        v += ch;
      break;
    }
  }
}

void resetV() {
  v = "";
}

void getAngles(String input, float *angles) {
  int comma_1 = 0;
  int comma_2 = 0;
  for (int i = 0; i < input.length(); i++) {
    if (input.substring(i, i+1) == ",") {
      if (comma_1 == 0) {
        comma_1 = i;
      } else {
        comma_2 = i;
      }
    }
  }
  angles[0] = input.substring(0, comma_1).toFloat();
  angles[1] = input.substring(comma_1+1, comma_2).toFloat();
  angles[2] = input.substring(comma_2+1, input.length()).toFloat();
}


void move(float* angles) {
  
  

      servoA.writeMicroseconds(floor(angles[0]*RATIO) + AZERO);
      servoB.writeMicroseconds(floor(angles[1]*BRATIO) + BZERO);
      servoC.writeMicroseconds(floor(angles[2]*CRATIO) + CZERO);
    
  }







