import sys
import serial
from time import sleep
from Library_Mbot_v1 import *
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Lee del sensor de distancia (ultrasonic) y enciende led rojo si la pared está muy cerca y verde si no")

serial = open_PortSerial('com3')


while 1:
  try:
    sensorMessage = read_Sensor(serial)    
    if (sensorMessage == -1):
        continue
    else:
      if (sensorMessage[0].lower() == 'distance'):
        if (sensorMessage[1] < 10):
          turnOn_Leds([0,255,0,0],serial)
        else:
          turnOn_Leds([0,0,255,0],serial)
  except KeyboardInterrupt:
    send_Quit(serial)
    break

sys.exit(0)

