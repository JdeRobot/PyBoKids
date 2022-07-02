# -- Aquí los módulos necesarios
import sys
import serial
from time import sleep
from Library_Mbot_v1 import *


#-- Poner aquí las variables globales, si se necesitan

#-- Sacar mensaje inicial: qué va a hacer el robot

Distancia_threshold = 10

while 1: # -- para que sea infinito
    try:
        sensorMessage = read_Sensor(serial)    
        if (sensorMessage == -1):
            continue
        else:
            if (sensorMessage[0].lower() == 'distance'):
                if (sensorMessage[1] < Distancia_threshold):
                    turnOn_Motors([100,100],serial)
                else:
                    turnOn_Motors([100,100],serial)
    except KeyboardInterrupt:
        send_Quit(serial)
        break

sys.exit(0)
