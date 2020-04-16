import serial
import threading
import json
import urllib.request
import requests
from twilio.rest import Client

global flag
flag = False

def post_cloud_humidity():
    global flag
    threading.Timer(17,post_cloud_humidity).start()
    val=read_data()
    # print(len(val))
    # print(val)
    my_hum,my_temp,my_aqi,my_press=val.split(",")
    url='https://api.thingspeak.com/update?api_key=F1C10T58VUV699X0&field1={}&field2={}&field3={}&field4={}'.format(my_hum,my_temp,my_aqi,my_press)
    data=urllib.request.urlopen(url)
    print(data)
    print(my_temp)
    print(type(my_temp))

    if my_temp >= str(29) or my_aqi > 200 or my_press>= 29:
        global flag
        if (not flag):
            # send_sms_alert(my_temp,my_hum,my_aqi,my_press)
            iftt(my_temp, my_hum, my_aqi,my_press)
            flag= True


def iftt(my_temp, my_hum, my_aqi, my_press):
    payload = { 'value1' : 'P', 'value2' : 'Q', 'value3' : 'R', 'value4' : 'S' }
    url='https://maker.ifttt.com/trigger/weather_alert_email/with/key/ingqu9FjtuppD0EMqCtMtsbgByhTsuRipYrOGeifvhl'
    payload['value1']=my_temp
    payload['value2']=my_hum
    payload['value3'] = str(my_aqi)+" Current Air Pressure : "+str(my_press)
    # payload['value4'] = my_press
    print(payload)
    requests.post(url, data=payload)
    print('Done')


def read_data():
    try:

        arduinodata =serial.Serial('COM5',9600, timeout=0.1)
        while arduinodata.inWaiting:
            val=arduinodata.readline().decode('ascii')
            print(val)
            print(len(val))
            if len(val)!=0 :
                return val
    except:
        print('Cannot read data !')

def send_sms_alert(my_temp, my_hum, my_aqi, my_press):

    try:

        my_body="Temperature is "+my_temp+"*C\nHumidity is "+my_hum+" %\nAir Quality Index"+my_aqi+" per cubic meter\nPressure is "+my_press+" Hg"

        client = Client('AC94fecc7af996b67eff01f18be67c9a2b','f5f466aaa86ddccea4fe5e39d095c782')
        client.messages.create(
                                from_= '+18317501217',
                                body=my_body,
                                 to='+918484994321')
    except:
        print('Cannot send Sms!')


if __name__ == '__main__':
    post_cloud_humidity()

