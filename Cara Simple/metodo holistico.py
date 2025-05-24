# -*- coding: utf-8 -*-
"""
Created on Mon May 12 09:01:41 2025

@author: Sahid
"""

import cv2
import mediapipe as mp

mp_holistico = mp.solutions.holistic
dibujar = mp.solutions.drawing_utils
estilo_dibujo = mp.solutions.drawing_styles

camara = cv2.VideoCapture(0)

# CORRECTO: solo una llamada al constructor
holistico = mp_holistico.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

while camara.isOpened():
    r, frame = camara.read()
    if not r:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    resultado = holistico.process(rgb)

    # Dibujo del rostro
    if resultado.face_landmarks:
        dibujar.draw_landmarks(
            frame,
            resultado.face_landmarks,
            mp_holistico.FACEMESH_CONTOURS,
            landmark_drawing_spec=dibujar.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1),
            connection_drawing_spec=dibujar.DrawingSpec(color=(0, 255, 0), thickness=1))
        
        dibujar.draw_landmarks(frame, resultado.pose_landmarks, mp_holistico.POSE_CONNECTIONS)
        
        dibujar.draw_landmarks(frame, resultado.left_hand_landmarks, mp_holistico.HAND_CONNECTIONS)
        
        dibujar.draw_landmarks(frame, resultado.right_hand_landmarks, mp_holistico.HAND_CONNECTIONS)

    cv2.imshow("Rostro", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
