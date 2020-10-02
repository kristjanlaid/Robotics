// The code blinks the center LED in the dot matrix.

// Defining row pins for ease of use.
// You should enter the pin numbers that you connected your display to.
int R1 = 2;
int R2 = 3;
int R3 = 4;
int R4 = 5;
int R5 = 6;
int R6 = 7;
int R7 = 8;

// The setup function runs once when you press reset or power the board.
void setup() {
// setting row pins as output pins.
// we can now just use the variable names for the pins that we defined above.
    pinMode(R1, OUTPUT);
    pinMode(R2, OUTPUT);
    pinMode(R3, OUTPUT);
    pinMode(R4, OUTPUT);
    pinMode(R5, OUTPUT);
    pinMode(R6, OUTPUT);
    pinMode(R7, OUTPUT);

// For start turn all the LED's off in the column.
    digitalWrite(R1, HIGH);
    digitalWrite(R2, HIGH);
    digitalWrite(R3, HIGH);
    digitalWrite(R4, HIGH);
    digitalWrite(R5, HIGH);
    digitalWrite(R6, HIGH);
    digitalWrite(R7, HIGH);
 }

// The loop function runs over and over again until the Arduino is powered on.
void loop() {
  digitalWrite(R1, LOW);
  delay(50);
  digitalWrite(R1, HIGH);
  digitalWrite(R2, LOW);
  delay(50);
  digitalWrite(R2, HIGH);
  digitalWrite(R3, LOW);
  delay(50);
  digitalWrite(R3, HIGH);
  digitalWrite(R4, LOW);
  delay(50);
  digitalWrite(R4, HIGH);
  digitalWrite(R5, LOW);
  delay(50);
  digitalWrite(R5, HIGH);
  digitalWrite(R6, LOW);
  delay(50);
  digitalWrite(R6, HIGH);
  digitalWrite(R7, LOW);
  delay(50);
  digitalWrite(R7, HIGH);
  digitalWrite(R6, LOW);
  delay(50);
  digitalWrite(R6, HIGH);
  digitalWrite(R5, LOW);
  delay(50);
  digitalWrite(R5, HIGH);
  digitalWrite(R4, LOW);
  delay(50);
  digitalWrite(R4, HIGH);
  digitalWrite(R3, LOW);
  delay(50);
  digitalWrite(R3, HIGH);
  digitalWrite(R2, LOW);
  delay(50);
  digitalWrite(R2, HIGH);
}
