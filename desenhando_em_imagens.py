import cv2

img = cv2.imread('img/ronaldo.jpeg')

#desenha linha
cv2.line(img, (277,180), (418,185), (0,255,0), 15)

#desenha retangulo
cv2.rectangle(img, (249,155), (455,207), (255,0,0), 3)

#desenha circulo
cv2.circle(img, (320,234), 50, (0,0,255), 3)

#desenha texto
cv2.putText(img, 'Ronaldo cascao', (249,100), cv2.FONT_HERSHEY_COMPLEX, 2, (255,255,0), 2, cv2.LINE_AA)

cv2.imshow('Ronaldo', img)

cv2.waitKey(0)

