// Ultrasonic sensor
int echo_pin = A4;
int trig_pin = A5;

// Line sensor
int ls1 = 2;
int ls2 = 3;
int ls3 = 4;
int ls4 = 5;
int ls5 = 6;

// Anything over 23200 us pulse (4000 mm) is "out of range"
const unsigned int ULTRASONIC_ECHO_TIMEOUT = 23200;

const int ULTRASONIC_DELAY = 10;
int us = 4000; // no reading, out of range value

void setup()
{
    Serial.begin(115200);
    // Set pin directions for the ultrasonic sensor
    pinMode(echo_pin, INPUT);
    pinMode(trig_pin, OUTPUT);

    // Set pin directions for the line sensor
    pinMode(ls1, INPUT);
    pinMode(ls2, INPUT);
    pinMode(ls3, INPUT);
    pinMode(ls4, INPUT);
    pinMode(ls5, INPUT);
}

void loop()
{
    // Get distance from wall with ultrasonic sensor
    us = get_US();
    
    // Read everything from serial
    if(Serial.available())
    {
        Serial.read();

        print_JSON(us); // Print data to serial.
    }


}

// Gets distance in mm from the ultrasonic sensor
long get_US()
{   delay(20);
    // TASK: get distance with ultrasonic, read about pulseIn() arguments and figure out how to use ULTRASONIC_ECHO_TIMEOUT
    digitalWrite(trig_pin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig_pin, LOW);
    delayMicroseconds(10);
    
    int duration = pulseIn(echo_pin, HIGH, ULTRASONIC_ECHO_TIMEOUT);
    int distance_in_mm = (duration / 2) / 2.91;
    
    return distance_in_mm;
}

// Print all the sensor data to serial as JSON
void print_JSON(int us)
{ 
    Serial.print("{\"us\":");
    Serial.print(us);
    Serial.print(", \"ls1\":");
    Serial.print(digitalRead(ls1));
    Serial.print(", \"ls2\":");
    Serial.print(digitalRead(ls2));
    Serial.print(", \"ls3\":");
    Serial.print(digitalRead(ls3));
    Serial.print(", \"ls4\":");
    Serial.print(digitalRead(ls4));
    Serial.print(", \"ls5\":");
    Serial.print(digitalRead(ls5));
    Serial.println("}");
}
