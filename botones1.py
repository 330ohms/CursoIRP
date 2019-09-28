import RPi.GPIO as GPIO
import time

pin_led = 17
pin_btn = 10

GPIO.setmode( GPIO.BCM )
GPIO.setup( pin_btn , GPIO.IN , pull_up_down=GPIO.PUD_UP )
GPIO.setup( pin_led , GPIO.OUT)
estado_led = False

try:
    while 1:
        if GPIO.input( pin_btn ) == GPIO.LOW:
            estado_led = not estado_led
            GPIO.output( pin_led , estado_led )
            print("Boton presionado")
            print("Estado " + str(estado_led) + "\n")
            time.sleep(0.3)

except KeyboardInterrupt:
    # CTRL+C
    print("\nInterrupcion por teclado")
except:
    print("Otra interrupcion")
finally:
    GPIO.cleanup()
    print("GPIO.cleanup() ejecutado")



