const int motor1Pin = 9;
const int motor2Pin = 10;

void setup() {
  Serial.begin(9600);
  pinMode(motor1Pin, OUTPUT);
  pinMode(motor2Pin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0){
    String msg = Serial.readString();

    if (msg == "ON"){
      // Turn both motors on
      digitalWrite(motor1Pin, HIGH);
      digitalWrite(motor2Pin, HIGH);
    }
    else if (msg == "OFF"){
      // Turn both motors off
      digitalWrite(motor1Pin, LOW);
      digitalWrite(motor2Pin, LOW);
    }
    else {
      // Blink both motors five times
      for (int i = 0; i < 5; i++){
        digitalWrite(motor1Pin, HIGH);
        digitalWrite(motor2Pin, HIGH);
        delay(100);
        digitalWrite(motor1Pin, LOW);
        digitalWrite(motor2Pin, LOW);
        delay(100);
      }
    }
  }
}
