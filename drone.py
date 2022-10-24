from turtle import color
import numpy as np
import cv2 as cv
from pyzbar.pyzbar import decode
cap = cv.VideoCapture('Drones.MP4')
cap.set(4,720)
cap.set(4,720)
dim = (720,720)
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv.resize(frame, dim, interpolation = cv.INTER_AREA)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
    for barcode in decode(frame):
        #print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int64)
        pts = pts.reshape((-1,1,2))
        cv.polylines(frame,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv.putText(frame,myData,(pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX,
        0.9,(255,0,255),2)
    #cv.imshow('Result',frame)
    cv.waitKey(1)
    #pasar ell bidero 




cap.release()
cv.destroyAllWindows()