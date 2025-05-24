# -*- coding: utf-8 -*-
"""
Created on Mon May 12 08:21:52 2025

@author: Sahid
"""

import cv2
import mediapipe as mp

mp_detectar_rostro = mp.solutions.face_detection
dibujar_rostro = mp.solutions.drawing_utils
detectar_cara = mp_detectar_rostro.FaceDetection(min_detection_confidence=0.5)

camara = cv2.VideoCapture(0)

while camara.isOpened():
    r, frame = camara.read()
    
    if not r:
        break
    
    frame = cv2.flip(frame, 1)
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    resultado = detectar_cara.process(rgb)
    
    if resultado.detections:
        for deteccion in resultado.detections:
            dibujar_rostro.draw_detection(frame, deteccion)
            
    cv2.imshow("Rostro", frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()