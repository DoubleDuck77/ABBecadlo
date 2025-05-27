import os
from PIL import Image
import numpy as np
import math
import cv2
import time

import cv2
import time
import os
from datetime import datetime


ODLEGLOSC = 200
POMARANCZOWY = (255, 165, 0)

SRODEK = (280, 230)
PUNKT3 = (0, SRODEK[1])

def newest(path):
    files = os.listdir(path)
    files = list(filter(lambda f: 'jpg' in f or 'png' in f, files))
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

def getAngle(a,b,c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang
def computeAngle(path):
    zdjecie = Image.open(newest(path))
    print(time.time)
    print(zdjecie.size)

    ok = []

    for x in range(0, zdjecie.size[0]):
        print(round(x/zdjecie.size[0]*100, 1),'%', end = '\r')
        for y in range(0, zdjecie.size[1]):
            pixel = zdjecie.getpixel((x, y))
                
            odl = sum([abs(pixel[c] - POMARANCZOWY[c]) for c in range(3)])
            
            if odl < ODLEGLOSC:
                zdjecie.putpixel((x, y), (255, 255, 255, 255))
                ok.append((x, y))
            else:
                zdjecie.putpixel((x, y), (0, 0, 0, 255))

    pixel = np.array(ok)
    np.random.seed(0)

    x = sum(pixel[:, 0]) / len(pixel[:, 0])
    y = sum(pixel[:, 1]) / len(pixel[:, 1])

    print(getAngle(PUNKT3, (x, y), SRODEK))

def capture_every_n_seconds(n, base_folder="/ABBecadlo/Software4camera/Pics"):

    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Cannot open camera")
        return
    try:
        while True:
            
            
            folder_path = base_folder
            os.makedirs(folder_path, exist_ok=True)

            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            filepath = os.path.join(folder_path, "test.jpg")

            cv2.imwrite(filepath, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
            computeAngle(folder_path)
            print(f"Saved {filepath}")

    finally:
        cap.release()

if __name__ == "__main__":
    capture_every_n_seconds(1)
