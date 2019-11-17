int SigPin = 8;
int NcPin = 9;
String Time = "";

void setup()
{
  pinMode(SigPin,OUTPUT);
  digitalWrite(SigPin, LOW);
  pinMode(NcPin,OUTPUT);
  digitalWrite(NcPin, LOW);

  Serial.begin(9600);
  while (!Serial);
}

void loop() 
{
  Serial.flush();
  Time = "";
  Time = Serial.readString();
  Serial.println(Time);
  
  digitalWrite(SigPin, HIGH);
  delay(Time.toInt());
  digitalWrite(SigPin, LOW);
  
  Serial.println("done");
}
