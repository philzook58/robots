#include <Servo.h>
//#include <SoftwareSerial.h>
#define ARATIO 425/(PI/4)
#define AZERO 1606
#define BZERO 1545
#define D 200.

Servo servoA, servoB;  // create servo object to control a servo
String v = "";
float x = 0.;
float y = 0.;


void setup()
{
  servoA.attach(9);
  servoB.attach(10);  // attaches the servo on pin 9 to the servo object
  move('a',0);
  move('b',0);
  Serial.begin(115200);
}

/*
void loop() {
  // put your main code here, to run repeatedly:
  
  
  if (Serial.available()) {
    char ch = Serial.read();
    //Serial.write(ch);
    
    switch(ch) {
      case ';':
        x = getX(v);
        y = getY(v);
        moveXY(x,y);
        //Serial.println(x);
        //Serial.println(y);
        resetV();
      break;
      default:
        v += ch;
      break;
    }
  }
}
*/

float t = 0;
void loop(){
   
  delay(50);
  t = t + 0.05;
  t = t % 1000;
  float x = 100*sin(3 * PI  * t / 5);
  float y = 100*sin(2 * PI * t / 5);
   moveXY(x,y); 
   
  
}
void resetV() {
  v = "";
}

float getX(String input) {
  int comma = 0;
  for (int i = 0; i < input.length(); i++) {
    if (input.substring(i, i+1) == ",") {
      comma = i;
    }
  }
  return input.substring(0, comma).toFloat();
}

float getY(String input) {
  int comma = 0;
  for (int i = 0; i < input.length(); i++) {
    if (input.substring(i, i+1) == ",") {
      comma = i;
    }
  }
  return input.substring(comma+1, input.length()).toFloat();
}


void move(char ch, float angle) {
  switch(ch) {
    case 'a':
      servoA.writeMicroseconds(floor(angle*ARATIO) + AZERO);
    break;
    case 'b':
      servoB.writeMicroseconds(floor(angle*ARATIO) + BZERO);
    break;
    
  }
}

void moveLineXY(float end_x, float end_y, int n_steps) {
  float start_x = x;
  float start_y = y;
  
  float delta_x = (end_x - start_x)/n_steps;
  float delta_y = (end_y - start_y)/n_steps;
  
  for (int i = 0; i < n_steps; i++) {
    moveXY(start_x + (delta_x * i), start_y + (delta_y * i));
    delay(5);
  }
}

void moveXY(float x, float y) {
  Serial.println(x);
  Serial.println(y);
  float r = getNorm(x,y,D);
  float vx = x/r;
  float vy = y/r;
  float vz = D/r;
  
  float nx = vx;
  float ny = vy - 1;
  float nz = vz;
 
  float nnorm = getNorm(nx,ny,nz);
  nx = nx/nnorm;
  ny = ny/nnorm;
  nz = nz/nnorm;
  
  float alpha = asin(nz);
  //float phi = atan2(y,x);
  float beta = atan2(nx,-ny);
  
  /*
  if (phi > PI/2) {
    phi = phi - PI;
    theta = theta * -1;
  } else if (phi < -PI/2) {
    phi = phi + PI;
    theta = theta * -1; 
  }
  */
  
  //Serial.println(alpha);
  //Serial.println(beta);
  
  move('a',alpha);
  move('b',-beta);
}

float getNorm(float x, float y, float z) {
  return sqrt(sq(x) + sq(y) + sq(z));
}
