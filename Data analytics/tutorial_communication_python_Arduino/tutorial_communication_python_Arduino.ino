const int sensorpin=A0;
const int AirValue = 520;   //you need to replace this value with Value_1
const int WaterValue = 260;  //you need to replace this value with Value_2
int intervals = (AirValue - WaterValue)/3;
int soilMoistureValue = 0;

int time=0;
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  soilMoistureValue=analogRead(sensorpin);
  if(soilMoistureValue > WaterValue && soilMoistureValue < (WaterValue + intervals))
{
  Serial.println(soilMoistureValue);
  Serial.println("Very Wet");

}
else if(soilMoistureValue > (WaterValue + intervals) && soilMoistureValue < (AirValue - intervals))
{
  Serial.println(soilMoistureValue);
  Serial.println("Wet");
  
}
else if(soilMoistureValue < AirValue && soilMoistureValue > (AirValue - intervals))
{
  Serial.println(soilMoistureValue);
  Serial.println("Dry");
}
  delay(1000);
  Serial.flush();
}
