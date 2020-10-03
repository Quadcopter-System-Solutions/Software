int incomingByte = 0;

void setup() {
  Serial.begin(9600); // open the serial port at 9600 bps:
}

void loop() {
  if (Serial.available() > 0) {
    Serial.println(char(Serial.read()));
  }
}
