import Adafruit_DHT as Sensor
import time

Outpin = 4

while True:
     Humi, Temp  = Sensor.read_retry(Sensor.DHT11, Outpin)
     print ("Humidity = {0:0.1f}% Temp = {1:0.1f}*C".format(Humi, Temp))
     time.sleep(1)