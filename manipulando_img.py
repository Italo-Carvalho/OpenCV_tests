import cv2

#pegar imagem
img = cv2.imread('img/ronaldo.jpeg')

#mostrar imagem
cv2.imshow("Ronaldo cascao" ,img)

#salvar nova imagem
cv2.imwrite('img/nova.jpeg', img)

#criar ROI
roi = img[75:350, 250:500]

#mostrar ROI
cv2.imshow("ROI" ,roi)

#image redimecionada
resize = cv2.resize(img, (200, 80))
#mostrar redimecionada
cv2.imshow("resize" ,resize)

#pausa
cv2.waitKey(0)