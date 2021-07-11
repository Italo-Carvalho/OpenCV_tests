import cv2

#0 vai procurar o primeiro dispositivo de video que ele achar
# em caso de stream passem a url ex: 'http://127.0.0.1:8000/videoaovivo'
# arquivo ex: 'img/video.mp4'
cap = cv2.VideoCapture('img/avenida.mp4')

while(True):
    #recuperar frame
    #ret = boolean frame=frame
    ret, frame = cap.read()
    if ret:
        #mostrar frame
        resize = cv2.resize(frame, (500, 300))
        cv2.imshow('frame', resize)
        
    
    #waitkey(ms)
    key = cv2.waitKey(180)
    if key == ord('q'):
        break

#libera o cache de cap
cap.release()

cv2.destroyAllWindows()