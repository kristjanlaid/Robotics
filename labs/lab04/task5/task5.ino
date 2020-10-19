#include <Servo.h>
#include <Wire.h>
#include <LPS.h>
#include <LIS3MDL.h>
#include <LSM6.h>
Servo myservo;
char report[80];
void enableDefault(void);
LPS ps;
LSM6 imu;
int x;
void setup() {
  myservo.attach(9);
  Serial.begin(9600);
  Wire.begin();

  ps.enableDefault();

  if (!imu.init())
  {
    Serial.println("Failed to detect and initialize IMU!");
    while (1);
  }
  imu.enableDefault();
}

void loop() {
  imu.read();

    snprintf(report, sizeof(report), "Accelerometer: %6d %6d %6d g-units   Gyroscope: %6d %6d %6d dps",
      imu.a.x, imu.a.y, imu.a.z,
      imu.g.x, imu.g.y, imu.g.z);
  //  Serial.println(report);
  Serial.println("A: ");
  Serial.print("X: ");
  Serial.print((imu.a.x)*0.000061);
  Serial.print(" g\nY: ");
  Serial.print((imu.a.y)*0.000061);
  Serial.print(" g\nZ: ");
  Serial.print((imu.a.z)*0.000061);
  Serial.println(" g ");
  
  Serial.println("G: ");
  Serial.print("X: ");
  Serial.print((imu.g.x));
  Serial.print(" dps\nY: ");
  Serial.print((imu.g.y));
  Serial.print(" dps\nZ: ");
  Serial.print((imu.g.z));
  Serial.println(" dps ");
  delay(100);

  x = map(imu.a.x,-16000, 16000, 1400, 1600);
  
  if(x >= 1400 and x <= 1600){
    myservo.writeMicroseconds(x);
  }
  Serial.println(x);

}
