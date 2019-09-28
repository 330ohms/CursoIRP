import sys
import time
import telepot
import RPi.GPIO as GPIO

pin_led = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT) 

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Recibí el mensaje: %s' % command)
    if command == 'on':
        bot.sendMessage(chat_id, 'encendiendo')
        GPIO.output(pin_led,GPIO.HIGH)
        print("Encendí el led")
    elif command =='off':
        bot.sendMessage(chat_id, 'apagando')
        GPIO.output(pin_led,GPIO.LOW)
        print("Apague el led")

try:
    bot = telepot.Bot("920687977:AAF2OsgWx6Kn6bt9CkoYPsMz1J9ynC8Rlj4")
    bot.message_loop(handle)
    print("Me presento:\n" + str(bot.getMe()))
    print('Estoy escuchando...')

    while 1:
        time.sleep(10)
except KeyboardInterrupt:
    print('\nInterrupción por teclado')
except:
    print('Otra interrupción')
finally:
    GPIO.cleanup()
    print("GPIO.cleanup() ejecutado")
    exit()
