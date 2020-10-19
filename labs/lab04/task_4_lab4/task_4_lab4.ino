#include <Wire.h>
#include <LPS.h>
#include <LIS3MDL.h>
#include <LSM6.h>

LSM6 imu;
LPS ps;
LIS3MDL mag;
char report[80];
void enableDefault(void);



void setup()
{
  Serial.begin(9600);
  Wire.begin();

  if (!ps.init())
  {
    Serial.println("Failed to autodetect pressure sensor!");
    while (1);
  }

  ps.enableDefault();

  if (!mag.init())
  {
    Serial.println("Failed to detect and initialize magnetometer!");
    while (1);
  }
  if (!ps.init())
  {
    Serial.println("Failed to autodetect pressure sensor!");
    while (1);
  }

  ps.enableDefault();

  if (!imu.init())
  {
    Serial.println("Failed to detect and initialize IMU!");
    while (1);
  }
  imu.enableDefault();
}

void loop()
{
  float pressure = ps.readPressureMillibars();
  float altitude = ps.pressureToAltitudeMeters(pressure);
  float temperature = ps.readTemperatureC();

  Serial.print("p: ");
  Serial.print(pressure);
  Serial.print(" mbar\ta: ");
  Serial.print(altitude);
  Serial.print(" m\tt: ");
  Serial.print(temperature);
  Serial.println(" °C ");

  delay(100);

  mag.read();

    snprintf(report, sizeof(report), "Magnetometer: %6d %6d %6d gauss",
      mag.m.x, mag.m.y, mag.m.z);
//    Serial.println(report);
  Serial.println("G: ");
  Serial.print("X: ");
  Serial.print((mag.m.x)*6842);
  Serial.print(" gauss\nY: ");
  Serial.print((mag.m.y)*6842);
  Serial.print(" gauss\nZ: ");
  Serial.print((mag.m.z)*6842);
  Serial.println(" gauss ");
  delay(100);

  delay(100);

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
  delay(100);
}
