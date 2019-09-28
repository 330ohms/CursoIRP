import RPi.GPIO as GPIO
import time

pin_rojo = 17
pin_amarillo = 27
pin_verde = 22
pin_btn1 = 10
pin_btn2 = 9


paso = False
encendido = False
parpadeo = True

def btn_cb1(channel):
	global paso
	if encendido:
		paso = True
	
def btn_cb2(channel):
	global encendido
	encendido = not encendido

GPIO.setmode( GPIO.BCM )
GPIO.setup( pin_rojo , GPIO.OUT)
GPIO.setup( pin_amarillo , GPIO.OUT)
GPIO.setup( pin_verde , GPIO.OUT)
GPIO.setup( pin_btn1 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
GPIO.setup( pin_btn2 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
GPIO.add_event_detect( pin_btn1 , GPIO.FALLING, callback=btn_cb1, bouncetime = 300)
GPIO.add_event_detect( pin_btn2 , GPIO.FALLING, callback=btn_cb2, bouncetime = 300)


try:
	while 1:
		if encendido:
			if not paso:
				GPIO.output( pin_rojo , False )
				GPIO.output( pin_amarillo , False )
				GPIO.output( pin_verde , True )
			else:
				GPIO.output( pin_rojo , False )
				GPIO.output( pin_amarillo , True )
				GPIO.output( pin_verde , False )
				time.sleep(0.5)
				GPIO.output( pin_amarillo , False )
				time.sleep(0.5)
				GPIO.output( pin_amarillo , True )
				time.sleep(0.5)
				GPIO.output( pin_amarillo , False )
				time.sleep(0.5)
				GPIO.output( pin_amarillo , True )
				time.sleep(0.5)
				GPIO.output( pin_amarillo , False )
				time.sleep(0.5)
				GPIO.output( pin_amarillo , True )
				time.sleep(0.5)
				GPIO.output( pin_amarillo , False )
				GPIO.output( pin_rojo , True )
				time.sleep(3)
				paso = False
		else:
			if parpadeo:
				GPIO.output( pin_amarillo , True )
				parpadeo = False
			else: 
				GPIO.output( pin_amarillo , False )
				parpadeo = True
			GPIO.output( pin_rojo , False )
			GPIO.output( pin_verde , False )
			time.sleep(0.5)


except KeyboardInterrupt:
    # CTRL+C
    print("\nInterrupcion por teclado")
except:
    print("Otra interrupcion")
finally:
    GPIO.cleanup()
    print("GPIO.cleanup() ejecutado")
