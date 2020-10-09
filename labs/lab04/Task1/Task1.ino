const int pir_pin = 5;           // passive infrared sensor pin
bool in_motion = false;
int ledState = LOW;
unsigned long previousMillis = 0;
const int ledPin =  LED_BUILTIN;
const long interval = 200;
bool blinking = false;

void setup(){
    Serial.begin(9600);          // initialize serial with 9600 baud rate
    pinMode(pir_pin, INPUT);     // set pin #5 as an input from PIR
    pinMode(ledPin, OUTPUT);
}


void loop(){
    unsigned long currentMillis = millis();
    
    if(digitalRead(pir_pin) == HIGH  &&  !in_motion){
      Serial.println("Motion detected!");
      in_motion = true;
      if(blinking == false){
        blinking = true;
      }  else {
        blinking = false;
      }
        
        
        
      }
      
    if(digitalRead(pir_pin) == LOW  &&  in_motion){
      Serial.println("No movement any more");
      in_motion = false;


    }

    if(blinking == true){
      if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;

      if (ledState == LOW) {
      ledState = HIGH;
    } else {
      ledState = LOW;
      }
      digitalWrite(ledPin, ledState);

      }
    }
    else{
            digitalWrite(ledPin, LOW);

    }
}



      
      
    
