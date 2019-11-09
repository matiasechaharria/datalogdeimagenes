#!/usr/bin/env python
import datetime
import time
import numpy as np
import cv2
import os
import sys
from playsound import playsound
from subprocess import call
import smtplib
import __future__
import pytesseract
import imutils
from matplotlib import pyplot as plt


#MINUTOS_SETUP= 300# 5minutos *60 ->300
MINUTOS_SETUP= 60* 3


cap = cv2.VideoCapture(1)  # camara externa
#cap = cv2.VideoCapture(0) # camara de la pc)

a = 0

#creo el directorio para las DataImagen#
if not os.path.exists("DataImagen"):
    os.makedirs("DataImagen")

now = datetime.datetime.now()
nowAux = str(now)
folder = nowAux[0:10]
if not os.path.exists("DataImagen/"+ folder):
    os.makedirs("DataImagen/"+ folder)
    print ("Carpeta creada:"+ "DataImagen/"+ folder)

print ("Formato: Imagen")
medicion = raw_input("Respeta el formato: ")

if not os.path.exists("DataImagen/"+ folder+"/"+ medicion):
    os.makedirs("DataImagen/"+ folder+"/"+ medicion)
    print ("Carpeta creada:"+"DataImagen/"+ folder+"/"+ medicion)

mesureDir= "DataImagen/"+ folder+"/"+ medicion
print (mesureDir)
#Comiezo del programa#
flag=0
#Acomode los termometros#
print ("Tiene 5 minutos para acomodar los termometros")

while(True):
    ret, frame = cap.read()
    # Our operations on the frame come here
    #cv2.imshow('frame',gray)
    cv2.imshow('setup',frame)

    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = 127

    a=a+1
    if MINUTOS_SETUP == a:#5minutos
          break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        flag=1
        break
    time.sleep(1)                                  #demora 1seg#


cv2.destroyAllWindows()
a=0
#Veo si corresponde iniciar las DataImagen o alguien apreto 'q'#
if flag==0:
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        #cv2.imshow('setup',frame)

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('Midiendo',gray)
        time.sleep(1)                                   #duerme el proceso#

        if 0 == a%60 : #minuto
            now = datetime.datetime.now()
            nameAux = str(now)
            name = nameAux[0:19]
            name = str(name)+".png"
            print(mesureDir+"/" + str(name))

            cv2.imwrite(mesureDir+"/" + str(name),frame)              #Guardo las fotos

        #if a == 540 :#10 fotos
        if a == 540*6 :#10 fotos
            a=0
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        a=a+1
        #print a

# When everything done, release the capture
cont = 0
while cont < 3:
    playsound('/home/matias/Documentos/Pruebas_Malbran/Trabajo_muy_duro.mp3')
    print (cont)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cont += 1  # This is the same as count = count + 1

cap.release()
cv2.destroyAllWindows()
