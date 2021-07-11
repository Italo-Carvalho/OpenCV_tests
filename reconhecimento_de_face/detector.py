# IMPORTS
import cv2
import os
import numpy as np
pathName = 'reconhecimento_de_face'
# funções
def savePerson():
    global ultimoNome
    global boolsaveimg
    name = input('Qual o seu nome?')
    ultimoNome = name
    boolsaveimg = True

def trainData():
    global recognizer
    global trained
    global persons
    trained = True
    persons = os.listdir(f'{pathName}/train')
    ids = []
    faces = []
    for i, p in enumerate(persons):

        for f in os.listdir(f'{pathName}/train/{p}'):
            img = cv2.imread(f'{pathName}/train/{p}/{f}', 0)
            faces.append(img)
            ids.append(i)

    recognizer.train(faces , np.array(ids))

def saveImg(img):
    global ultimoNome 
    if not os.path.exists(f'{pathName}/train'):
        os.makedirs(f'{pathName}/train')
    if not os.path.exists(f'{pathName}/train/{ultimoNome}'):
        os.makedirs(f'{pathName}/train/{ultimoNome}')

    files = os.listdir(f'{pathName}/train/{ultimoNome}')
    cv2.imwrite(f'{pathName}/train/{ultimoNome}/{str(len(files))}.jpg', img)


ultimoNome = ''

boolsaveimg = False

trained = False

savecount = 0

persons = []

recognizer = cv2.face.LBPHFaceRecognizer_create()

# READ VIDEO
cap = cv2.VideoCapture(0)

# LOAD HAAR CASCADE CLASSIFIER
face_cascade = cv2.CascadeClassifier('reconhecimento_de_face/haarcascade_frontalface_default.xml')

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

        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi,(50,50))
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

        if trained:
            idf, conf = recognizer.predict(roi)
            nameP = persons[idf]
            cv2.putText(frame, nameP, (x-y,y), 0, 1.5, (0,20,220), 1)

        if boolsaveimg:
            saveImg(roi)
            savecount += 1

        if savecount > 50:
            boolsaveimg = False
            savecount = 0



        
    # SHOW FRAME
    cv2.imshow('frame',frame)

    # WAITKEY
    key = cv2.waitKey(1) 

    if key == ord('s'):
        savePerson()

    # treinar imagens
    if key == ord('t'):
        trainData()

    if key == ord('q'):
        break

# RELEASE CAP
cap.release()

# DESTROY ALL WINDOWS
cv2.destroyAllWindows()