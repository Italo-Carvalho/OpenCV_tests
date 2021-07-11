import cv2
import numpy as np


def nothing(x):
    pass

#criar janela de trackbars
cv2.namedWindow('track')

#criar as trackbars
cv2.createTrackbar('th', 'track', 150, 255, nothing)
cv2.createTrackbar('ero', 'track', 1, 10, nothing)
cv2.createTrackbar('dil', 'track', 1, 10, nothing)
cv2.createTrackbar('opn', 'track', 1, 10, nothing)
cv2.createTrackbar('clo', 'track', 1, 10, nothing)

cap = cv2.VideoCapture('img/avenida.mp4')

while(True):
    # recuperar trackbar
    th = cv2.getTrackbarPos('th', 'track')
    ero = cv2.getTrackbarPos('ero', 'track')
    dil = cv2.getTrackbarPos('dil', 'track')
    opn = cv2.getTrackbarPos('opn', 'track')
    clo = cv2.getTrackbarPos('clo', 'track')
    ret, frame = cap.read()

    # criar frame preto e branco
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # criar kernel 
    kernel = np.ones((5,5), np.uint8)

    # criar blur
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # criar threshold
    ret, thres = cv2.threshold(blur, th, 255, cv2.THRESH_BINARY_INV)

    # erosao
    erosion = cv2.erode(thres, kernel, iterations=ero)

    # dilatação
    dilate = cv2.dilate(thres, kernel, iterations=dil)

    # oppening
    opening = cv2.morphologyEx(thres, cv2.MORPH_OPEN, kernel, iterations=opn)

    #closing
    closing = cv2.morphologyEx(thres, cv2.MORPH_CLOSE, kernel, iterations=clo)

    cv2.imshow('closing', closing)
    if cv2.waitKey(60) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()