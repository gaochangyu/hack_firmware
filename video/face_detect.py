import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
classfier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
color = (0, 0, 0)

print time.clock()

global lastUploadTime

def uploadPic():
    pass

def faceRecognize():
    success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.equalizeHist(gray, gray)
    faceRects = classfier.detectMultiScale(gray, 1.3, 5)
    if len(faceRects) > 0:
        for faceRect in faceRects:
                x, y, w, h = faceRect
                #cv2.rectangle(frame, (x, y), (x+w, y+h), color)
                cv2.circle(frame,(x+w/2,y+h/2),w/2,color,2,8,0)
        cv2.imwrite("face.jpg", frame)
        if time.clock() - lastUploadTime >= 1:
            uploadPic()
            lastUploadTime = time.clock()
    cv2.imshow("face", frame)


if __name__ == '_main__':
    lastUploadTime = 0
    while(True):
        faceRecognize()
        key = cv2.waitKey(10)
        c = chr(key & 255)
        if c in ['q', 'Q', chr(27)]:
            break
    cv2.destroyAllWindows
