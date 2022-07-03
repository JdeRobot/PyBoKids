# -- Esto es un comentario

# -- Aquí los módulos necesarios
import sys
from turtle import color
import serial
from time import sleep
from Library_Mbot_v1 import *


#-- Poner aquí las variables globales, si se necesitan

#-- Sacar mensaje inicial: qué va a hacer el robot
while 1:
    try:
        #--Escribe aquí el programa principal
        print ("Escribe lo que quieres hacer: quit, leds, motores, o zumbador")
        cadena=input()
        if (cadena.lower() == 'quit'):
            send_Quit(serial)
            break
        elif (cadena.lower() == 'leds'):
            print ("Color?: rojo, azul, verde")
            cadenacolor=input()
            if (cadenacolor.lower() == 'red'):
                turnOn_Leds([0,255,0,0],serial)
            elif (cadenacolor.lower() == 'verde'):
                turnOn_Leds([0,0,255,0],serial)
            elif (cadenacolor.lower() == 'azul'):
                turnOn_Leds([0,0,0,255],serial)
            else:
                print ("color equivocado")
                continue
        elif (cadena.lower() == 'motores'):
            print ("rapido o lento?")
            cadenavelocidad = input()
            if (cadenavelocidad.lower() == 'rapido'):
                turnOn_Motors([255,255],serial)
            if (cadenavelocidad.lower() == 'lento'):
                turnOn_Motors([100,100],serial)
            else:
                print ("velocidad equivocada")
                continue
        elif (cadena.lower() == 'motores'):
            print ("agudo o grave?")
            cadenanota = input()
            if (cadenanota.lower() == 'agudo'):
                turnOn_Buzzer([659,3],serial)
            elif (cadenanota.lower() == 'grave'):
                turnOn_Buzzer([73,3],serial)
            else:
                print("opcion equivocada")
                continue
        else:
            print("No te he entendido. Escribe exactamente la orden")
            continue
        
    except KeyboardInterrupt:
        send_Quit(serial)

sys.exit(0)