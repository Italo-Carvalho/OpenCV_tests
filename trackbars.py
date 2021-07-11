import cv2

def nothing(x):
    pass

#criar janela de trackbars
cv2.namedWindow('trackbars')

#criar as trackbars
cv2.createTrackbar('x', 'trackbars', 0, 800, nothing)
cv2.createTrackbar('y', 'trackbars', 0, 800, nothing)
cv2.createTrackbar('w', 'trackbars', 100, 800, nothing)
cv2.createTrackbar('h', 'trackbars', 100, 800, nothing)

cap = cv2.VideoCapture('img/avenida.mp4')

while(True):
    # recuperar trackbar
    x = cv2.getTrackbarPos('x', 'trackbars')
    y = cv2.getTrackbarPos('y', 'trackbars')
    w = cv2.getTrackbarPos('w', 'trackbars')
    h = cv2.getTrackbarPos('h', 'trackbars')
    ret, frame = cap.read()
    roi = frame[y:h, x:w]
    cv2.imshow('frame', roi)
    if cv2.waitKey(200) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()