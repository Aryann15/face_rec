import os
import cv2 as cv
import numpy as np

people = ['Robert Downey jr.', 'Chris Evans', 'Chris Hemsworth', 'Jeremy Renner', ' Mark Ruffalo','Scarlett Johansson']
DIR = r'C:\Users\rajly\OneDrive\New folder'

features = []
labels = []

def create_label():
    for person in people:
        path  = os.path.join(DIR, person)
        label =people.index()

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
