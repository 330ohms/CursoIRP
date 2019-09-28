import RPi.GPIO as GPIO
import time



pin_led = 17
pin_btn = 10
estado_led = False

def button_callback(channel):
    global estado_led
    estado_led = not estado_led
    GPIO.output( pin_led , estado_led )
    print("Boton presionado")
    print("Estado " + str(estado_led) + "\n")

GPIO.setmode( GPIO.BCM )
GPIO.setup( pin_btn , GPIO.IN , pull_up_down=GPIO.PUD_UP )
GPIO.add_event_detect( pin_btn , GPIO.FALLING, callback=button_callback, bouncetime = 300)
GPIO.setup( pin_led , GPIO.OUT)


try:
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    # CTRL+C
    print("\nInterrupcion por teclado")
except:
    print("Otra interrupcion")
finally:
    GPIO.cleanup()
    print("GPIO.cleanup() ejecutado")



