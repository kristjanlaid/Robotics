#include <Servo.h>
Servo my_servo;
int x = 0;
boolean turn180 = true;
void setup() {
  my_servo.attach(5);
}

void loop() {
  if (x == 180){
    turn180 = false;
  }
  if (x == 0){
    turn180 = true;
  }

  if (turn180 == true){
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
