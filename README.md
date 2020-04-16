 # Important things before kicking off
 
 ## Please import all suitable libraries

1. Create ThingSpeak account and create 4 channels for temperature, humidity, pressure, air quality index.
2. Copy the write API key and paste in 'arduino_thingspeak.py' file.
3. Create IFTTT account and create Applet. (If web_hooks Than mail)
https://saltillo.com/support/article/webhook-example-sending-an-email
4. Go through above link and add 3 values for temperature, humidity and air quality index.
5. Enter details as shown in Body section "Current Temperature : {{Value1}} Current Humidity : {{Value2}} Current Air Quality Index : {{Value3}}".
6. Instead of 'weather_alert_email' enter your event name.
7. For twilio integration go through "https://www.twilio.com/docs/sms/send-messages".
8. Upload Code to arduino.
9. Do connection as follows

DHT-11 (data pin - A0, VIN - 5V),
MQ-135 (AO-A1, VIN - 5V),
BMP-180 (SCL - A5, SDA - A4, VIN - 3.3V)

10. First connect all components and turn on Arduino with supply.
11. DON'T OPEN SERIAL MONITOR OTHERWISE PYTHON CANNOT READ DATA !
12. Keep running arduino in background and run python script.
13. After 15 seconds of interval python script will read data and send to server.
14. Once temperature exceeds 29 degrees, it sends user notification mail.
