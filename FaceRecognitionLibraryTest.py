#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 11:15:41 2020

@author: michaelhyh
"""
import cv2
import face_recognition
video_capture = cv2.VideoCapture(0)

face_locations=[]

while True:
  ret, frame = video_capture.read()
  rgb_frame = frame[:, :, ::-1]

  face_locations = face_recognition.face_locations(rgb_frame)

  for y2, x2, y1, x1 in face_locations:
    cv2.rectangle(frame, (x1, y2), (x2, y1), (0,0,255), 2)

  cv2.imshow('Video', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video_capture.release()
cv2.destroyAllWindows()