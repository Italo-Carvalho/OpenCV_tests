import cv2
import numpy as np


def nothing(x):
    pass

#criar janela de trackbars
cv2.namedWindow('track')

#criar as trackbars
cv2.createTrackbar('l-h', 'track', 0, 255, nothing)
cv2.createTrackbar('l-s', 'track', 0, 255, nothing)
cv2.createTrackbar('l-v', 'track', 0, 255, nothing)
cv2.createTrackbar('u-h', 'track', 255, 255, nothing)
cv2.createTrackbar('u-s', 'track', 255, 255, nothing)
cv2.createTrackbar('u-v', 'track', 255, 255, nothing)

cap = cv2.VideoCapture(0)

while(True):
    # recuperar trackbar
    lh = cv2.getTrackbarPos('l-h', 'track')
    ls = cv2.getTrackbarPos('l-s', 'track')
    lv = cv2.getTrackbarPos('l-v', 'track')
    uh = cv2.getTrackbarPos('u-h', 'track')
    us = cv2.getTrackbarPos('u-s', 'track')
    uv = cv2.getTrackbarPos('u-v', 'track')



    ret, frame = cap.read()

    # criar lower e upper
    lowwer = np.array([lh,ls,lv])
    upper = np.array([uh,us,uv])

    # converter rgb para hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    # criar mascara
    mask = cv2.inRange(hsv, lowwer, upper)

    # detectar contorno
    contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    #desenhar contornos
    cv2.drawContours(frame, contours, -1, (255,0,0), 3)
    
    cv2.imshow('mask', frame)
    if cv2.waitKey(60) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()