// LDR Module Oscilloscope Code
// Connections:
// VCC -> 5V
// GND -> GND
// AO  -> A0
// DO  -> Not Connected

const int sensorPin = A0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(sensorPin);

  // Send value to Python/Web Dashboard
  Serial.println(sensorValue);

  // ~200 samples per second
  delay(5);
}