# IMPORTS
import numpy as np
import cv2

# READ VIDEO
cap = cv2.VideoCapture(0)

# LOAD HAAR CASCADE CLASSIFIER
face_cascade = cv2.CascadeClassifier('detector_de_face/haarcascade_frontalface_default.xml')

# LOOP
while(True):
    
    # READ FRAME
    _, frame = cap.read()

    # GRAY FRAME
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # DETECT FACES IN FRAME
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # RUN ALL FACES IN FRAME
    for (x,y,w,h) in faces:
        # DRAW RECT IN FACE
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    # SHOW FRAME
    cv2.imshow('frame',frame)

    # WAITKEY
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

# RELEASE CAP
cap.release()

# DESTROY ALL WINDOWS
cv2.destroyAllWindows()