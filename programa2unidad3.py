# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 08:30:52 2025

@author: Sahid

rojo claro 0,100,20
rojo oscuro 5,255,255

rojo claro2 175,100,20
rojo oscuro 2 179,255,255

verde claro 25,25,20
verde oscuro 100,255,255

azul claro 100,100,20
azul oscuro 125,255,255

"""


"""COLOR VERDE'''
'''
import cv2
import numpy as np

img = cv2.imread('rgb.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
verdeclaro = np.array([25,20,20], np.uint8)
verdeoscuro = np.array([100,255,255], np.uint8)

'''verdeclaro = np.array([25,20,20], np.uint8)
verdeoscuro = np.array([100,255,255], np.uint8)'''

mascara = cv2.inRange(img2, verdeclaro, verdeoscuro)

'''mascara = cv2.inRange(img2, verdeclaro, verdeoscuro)'''


kernel = np.ones((7,7), np.uint8)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
seleccion = cv2.bitwise_and(img, img, mask=mascara)
contorno, valor = cv2.findContours(mascara.copy(), cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

cv2.namedWindow('resultado',cv2.WINDOW_NORMAL)
cv2.imshow('resultado', seleccion)

seleccion[mascara>0]=(255,255,255)
cv2.namedWindow('cambio',cv2.WINDOW_NORMAL)
cv2.imshow('cambio', seleccion)

cv2.namedWindow('original',cv2.WINDOW_NORMAL)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""


'''COLOR ROJO'''
'''
import cv2
import numpy as np

img = cv2.imread('rgb.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rojoclaro1 = np.array([0,100,20], np.uint8)
rojooscuro1 = np.array([5,255,255], np.uint8)
rojoclaro2 = np.array([175,100,20], np.uint8)
rojooscuro2 = np.array([179,255,255], np.uint8)

mascara1 = cv2.inRange(img2, rojoclaro1, rojooscuro1)
mascara2 = cv2.inRange(img2, rojoclaro2, rojooscuro2)
mascara = cv2.add(mascara1, mascara2)

seleccion = cv2.bitwise_and(img, img, mask=mascara)
contorno, valor = cv2.findContours(mascara.copy(), cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

cv2.namedWindow('resultado',cv2.WINDOW_NORMAL)
cv2.imshow('resultado', seleccion)

seleccion[mascara>0]=(255,255,255)
cv2.namedWindow('cambio',cv2.WINDOW_NORMAL)
cv2.imshow('cambio', seleccion)

cv2.namedWindow('original',cv2.WINDOW_NORMAL)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''COLOR AZUL'''

'''
import cv2
import numpy as np

img = cv2.imread('rgb.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
azulclaro = np.array([100,100,20], np.uint8)
azuloscuro = np.array([125,255,255], np.uint8)
mascara = cv2.inRange(img2, azulclaro, azuloscuro)
kernel = np.ones((7,7), np.uint8)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
seleccion = cv2.bitwise_and(img, img, mask=mascara)
contorno, valor = cv2.findContours(mascara.copy(), cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

cv2.namedWindow('resultado',cv2.WINDOW_NORMAL)
cv2.imshow('resultado', seleccion)

seleccion[mascara>0]=(255,255,255)
cv2.namedWindow('cambio',cv2.WINDOW_NORMAL)
cv2.imshow('cambio', seleccion)

cv2.namedWindow('original',cv2.WINDOW_NORMAL)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
