#include <Servo.h>
Servo myservo;
unsigned long StartTime = millis();
const long interval = 10;
unsigned long previousMillis = 0;
int sensorValue = 50;
bool in_motion = false;
int input;
#define MAX_PWM 1600
#define MID_PWM 1500
#define MIN_PWM 1400

void setup() {
  pinMode(A0, INPUT);
  Serial.begin(9600);
  myservo.attach(9);


}

void loop() {
  unsigned long currentMillis = millis();
  if(Serial.available() > 0){
    input = Serial.parseInt();
    myservo.writeMicroseconds(input);
  }
  sensorValue = analogRead(A0);
  if (sensorValue <= 50 && !in_motion) {
    in_motion = true;
    Serial.println((currentMillis - previousMillis) / 60);
    previousMillis = currentMillis;
    
  }

  if (sensorValue >= 120 && in_motion) {
    in_motion = false;
  }
   

}
