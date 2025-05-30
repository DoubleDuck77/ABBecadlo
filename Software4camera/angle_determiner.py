import os
from PIL import Image
import numpy as np
import math
import time

import cv2
import os
from datetime import datetime


ODLEGLOSC = 300
KOLOR = (0, 255, 0)
SRODEK = (280, 230)
PUNKT3 = (0, SRODEK[1])

cap = cv2.VideoCapture(19)
def newest(path):
    files = os.listdir(path)
    files = list(filter(lambda f: 'jpg' in f or 'png' in f, files))
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)


def getAngleFromPoints(a,b,c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang


def getAngleFromImage(path):
    zdjecie = Image.open(newest(path))

    ok = []

    for x in range(0, zdjecie.size[0]):
        print(round(x/zdjecie.size[0]*100, 1),'%', end = '\r')
        for y in range(0, zdjecie.size[1]):
            pixel = zdjecie.getpixel((x, y))
                
            odl = sum([abs(pixel[c] - KOLOR[c]) for c in range(3)])
            
            if odl < ODLEGLOSC:
                ok.append((x, y))
            else:
                zdjecie.putpixel((x, y), (0, 0, 0, 255))
    zdjecie.show()
    pixel = np.array(ok)
    np.random.seed(0)
    try:
        x = sum(pixel[:, 0]) / len(pixel[:, 0])
        y = sum(pixel[:, 1]) / len(pixel[:, 1])

        return (getAngleFromPoints(PUNKT3, (x, y), SRODEK))
    except:
        return -1

def takePhoto(path="./antena.jpg"):
    os.system("libcamera-still --width 800 --height 600 --timeout 30 -o " + path)

