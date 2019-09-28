import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor = Adafruit_DHT.DHT11
pin_sensor = 4
pin_btn = 10

def button_callback(channel):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_sensor)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

GPIO.setmode( GPIO.BCM )
GPIO.setup( pin_btn , GPIO.IN , pull_up_down=GPIO.PUD_UP )
GPIO.add_event_detect( pin_btn , GPIO.FALLING, callback=button_callback, bouncetime = 300)

while 1:
    time.sleep(2)
