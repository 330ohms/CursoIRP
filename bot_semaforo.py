import sys
import telepot
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


def handle(msg):
	global paso
	global encendido
	chat_id = msg['chat']['id']
	command = msg['text']
	print('Recibi el mensaje: %s' % command)
	if command == 'on':
		encendido = True
	elif command =='off':
		encendido = False
	elif command =='paso':
		if encendido:
			paso = True
try:
	bot = telepot.Bot("920687977:AAF2OsgWx6Kn6bt9CkoYPsMz1J9ynC8Rlj4")
	bot.message_loop(handle)
	print("Me presento:\n" + str(bot.getMe()))
	print('Estoy escuchando...')

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
	print('\nInterrupcion por teclado')
except:
	print('Otra interrupcion')
finally:
	GPIO.cleanup()
	print("GPIO.cleanup() ejecutado")
	exit()
