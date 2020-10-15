#include "Servo.h"
Servo myservo;
#define MAX_PWM 1600
#define MID_PWM 1500
#define MIN_PWM 1400
int input;
const int pir_pin = 5;
bool in_motion = false;
bool moving = false;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
  myservo.writeMicroseconds(1550);
  pinMode(pir_pin, INPUT);

}

void loop() {
  //  if(Serial.available() > 0){
  //    input = Serial.parseInt();
  //    if(input >= 1400 and input <= 1600){
  if (digitalRead(pir_pin) == HIGH && !in_motion) {
    Serial.println("In motion");
    in_motion = true;
    if (moving == false) {
      moving = true;
    } else {
      moving = false;
    }
  }

  if (digitalRead(pir_pin) == LOW && in_motion) {
    Serial.println("Not in motion");
    in_motion = false;
  }

  if (moving == false) {
    myservo.writeMicroseconds(1600);
  } else {
    myservo.writeMicroseconds(1500);

  }



}
