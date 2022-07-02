# -- Esto es un comentario

# -- Aquí los módulos necesarios
import sys
import serial
from time import sleep
from Library_Mbot_v1 import *


#-- Poner aquí las variables globales, si se necesitan

#-- Sacar mensaje inicial: qué va a hacer el robot

try:
    #--Escribe aquí el programa principal
    functions_mbot()
except KeyboardInterrupt:
    send_Quit(serial)

sys.exit(0)