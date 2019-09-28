import RPi.GPIO as GPIO
import time

pin = 17

GPIO.setmode(GPIO.BCM) #Pines segun el chip
#GPIO.setmode(GPIO.BOARD)  #Pines segun el orden
GPIO.setup(pin, GPIO.OUT)

try:
    while 1:
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    # CTRL+C
    print("Interrupcion por teclado")

except:
    print("otra interrupcion")

finally:
    GPIO.cleanup() 
    print("Se limpiaron GPIOs")
    exit()

