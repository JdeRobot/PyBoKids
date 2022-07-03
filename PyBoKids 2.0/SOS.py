# -- Esto es un comentario

# -- Aquí los módulos necesarios
import sys
import serial
from time import sleep
from Library_Mbot_v1 import *

#-- Poner aquí las variables globales, si se necesitan
serial = open_PortSerial('com3')
#-- Sacar mensaje inicial: qué va a hacer el robot
print ("Mensaje de socorro con el zumbador")

try:
    #--Escribe aquí el programa principal
    Mensaje_Zumbador_punto = ask_Message_Buzzer(serial)
    Mensaje_Zumbador_raya = ask_Message_Buzzer(serial)
    for i in range(6):
        for i in range (3):
            turnOn_Buzzer(Mensaje_Zumbador_punto,serial)
        for i in range (3):
            turnOn_Buzzer(Mensaje_Zumbador_raya,serial)
        for i in range (3):
            turnOn_Buzzer(Mensaje_Zumbador_punto,serial)
        sleep(3)
    send_Quit(serial)
except KeyboardInterrupt:
    send_Quit(serial)

sys.exit(0)