# -- Esto es un comentario

# -- Aquí los módulos necesarios
import sys
import serial
from time import sleep
from Library_Mbot_v1 import *


#-- Poner aquí las variables globales, si se necesitan

#-- Sacar mensaje inicial: qué va a hacer el robot
while 1
    try:
        #--Escribe aquí el programa principal
        print ("Escribe lo que quieres hacer: quit, leds, motores, o zumbador")
        cadena=input()
        if (cadena.lower() == 'quit'):
            send_Quit(serial)
            break
        elif (cadena.lower() == 'leds'):
            

        else:
            print("No te he entendido. Escribe exactamente la orden")
            continue
    except KeyboardInterrupt:
        send_Quit(serial)

sys.exit(0)