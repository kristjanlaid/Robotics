void setup() {
    Serial.begin(9600);
    Serial.println("Hello!");
    Serial.println("Please enter a number and press ENTER.");
}

void loop() {
      if (Serial.available()){
      int (m) = Serial.parseInt();
      if (m == 300){
      Serial.println("GO");
      }
      if (m > 300){
        Serial.println("STOP");
      }
      if (m < 300){
      Serial.println("STOP");
      }
      }
}
