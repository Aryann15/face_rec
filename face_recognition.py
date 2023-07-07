import numpy as np
import cv2 as cv

haar_cascade= cv.CascadeClassifier('haar_face.xml')

people = ['Robert downey jr', 'chris evans', 'chris hemsworth', 'jeremy renner', 'mark ruffalo','scarlett johanson']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img= cv.imread(r'C:\Users\rajly\OneDrive\Desktop\validation\evans.jpeg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

