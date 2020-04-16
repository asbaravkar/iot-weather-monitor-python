
#include <dht.h>
#define dht_apin A0 // Analog Pin sensor is connected to
#include <SFE_BMP180.h>
#include <Wire.h>

SFE_BMP180 pressure;
dht DHT;

int sensorValue;
int digitalValue;
 
void setup(){
 
  Serial.begin(9600);
  pressure.begin();
}
 
void loop(){
  
    char status;
    double T,P;
    
    DHT.read11(dht_apin);
    status = pressure.startPressure(3);
    status = pressure.getPressure(P,T);
    
    sensorValue = analogRead(1); // read analog input pin 0
    
    Serial.print(DHT.humidity);
    
    Serial.print(",");
    
    Serial.print(DHT.temperature); 

    Serial.print(",");

    Serial.print(sensorValue, DEC); // prints the value read
    
    Serial.print(",");
    
    Serial.print(P*0.0295333727,2);
    
    Serial.print("\n");
}// end loop(
