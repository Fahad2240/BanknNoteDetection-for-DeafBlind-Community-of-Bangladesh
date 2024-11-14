const int motor1Pin = 9;

void setup() {
  Serial.begin(9600);
  pinMode(motor1Pin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readString();

    if (msg == "2") {
      activateMotorNTimes(1);
    } else if (msg == "5") {
      activateMotorNTimes(2);
    } else if (msg == "10") {
      activateMotorNTimes(3);
    }else if (msg == "20") {
      activateMotorNTimes(4);
    }else if (msg == "50") {
      activateMotorNTimes(5);
    }else if (msg == "100") {
      activateMotorNTimes(6);
    }
    else if (msg == "200") {
      activateMotorNTimes(7);
    }
    else if (msg == "500") {
      activateMotorNTimes(8);
    }else if (msg == "1000") {
      activateMotorNTimes(9);
    }
  }
}

void activateMotorNTimes(int n) {
  for (int i = 0; i < n; i++) {
    digitalWrite(motor1Pin, HIGH);
    delay(500);  // Adjust delay time as needed
    digitalWrite(motor1Pin, LOW);
    delay(500);  // Adjust delay time as needed
  }
}
