import angle_determiner
from time import sleep, time
import json
import chamber as motor

N = 10

pomiary = dict()
for _ in range(N):
    start = time()
    motor.move()
    sleep(0.5)
    
    angle_determiner.takePhoto()
    angle = angle_determiner.getAngleFromImage(".")
    print(angle, time()-start)

    

