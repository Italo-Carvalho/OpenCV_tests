# IMPORTS
import cv2
import numpy as np

# READ VIDEO
cap = cv2.VideoCapture("img/avenida.mp4")
# cap = cv2.VideoCapture(0)

# CREATE SUBTRACTOR
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

# LOOP
while True:
     
    # READ FRAME
    _, frame = cap.read()

    # BLUR FRAME
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # CREATE MASK USING THE SUBTRACTOR AND ACTUAL FRAME
    mask = subtractor.apply(frame)

    # REMOVE SHADOW
    ret, mask = cv2.threshold(mask,220,255,cv2.THRESH_BINARY)

    # CREATE KERNEL
    kernel = np.ones((2,2),np.uint8)
    
    # OPENING
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations = 2)

    # FIND CONTOURS
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # RUN ALL CONTOURS
    for cnt in contours:

        # CONTOUR AREA
        area = cv2.contourArea(cnt)

        # CHECK IF AREA IS LARGE ENOUGH
        if area > 120:
            
            # BOUNDING RECT THE CONTOUR
            x,y,w,h = cv2.boundingRect(cnt)

            # DRAW RECT IN FRAME
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


    # SHOW FRAME
    cv2.imshow("Frame", frame)

    # SHOW MASK
    cv2.imshow("mask", mask)


    # WAITKEY
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# RELEASE CAP
cap.release()

# DESTROY ALL WINDOWS
cv2.destroyAllWindows()