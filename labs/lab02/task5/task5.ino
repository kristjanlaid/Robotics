#include <Servo.h>
Servo my_servo;
int x = 0;
boolean turn180 = true;

int echo_pin = 2;
int trig_pin = 3;
int delay_us = 10;
long distance_mm = 0;
long duration_us;

void setup() {
  my_servo.attach(5);
  Serial.begin(9600);
  pinMode(echo_pin, INPUT);
  pinMode(trig_pin, OUTPUT);
}

void loop() {
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);


  duration_us = pulseIn(echo_pin, HIGH);

  distance_mm = duration_us * 0.34 / 2;
  Serial.println(distance_mm);
  if (distance_mm > 300){
    my_servo.write(x);
 
  if (x == 180) {
    turn180 = false;
  }
  if (x == 0) {
    turn180 = true;
  }

  if (turn180 == true) {
    x += 1;
    my_servo.write(x);
  }

  my_servo.write(x);
  delay(10);


  if (turn180 == false)
  {
    x -= 1;
    my_servo.write(x);

    my_servo.write(x);
    delay(1);
  }

  }
}
