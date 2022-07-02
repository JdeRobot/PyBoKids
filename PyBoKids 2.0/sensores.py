# -- Esto es un comentario

# -- Aquí los módulos necesarios
import sys
import serial
from time import sleep
from Library_Mbot_v1 import *


#-- Poner aquí las variables globales, si se necesitan
serial = open_PortSerial('com3')
#-- Sacar mensaje inicial: qué va a hacer el robot
print ("Lee de los sensores para distinguir de cual viene el mensaje")


try:
    #--Escribe aquí el programa principal
    sensorMessage = read_Sensor(serial)
    if (sensorMessage == -1):
        pass
    else:
        if (sensorMessage[0] == 'distance'):
            print ("distance: " + sensorMessage[1])
        elif (sensorMessage[0] == 'siguelineas'):
            print ("siguelíneas: " + sensorMessage[1])
        elif (sensorMessage[0] == 'luz'):
            print ("sensor de luz: " + sensorMessage[1])
except KeyboardInterrupt:
    send_Quit(serial)

sys.exit(0)