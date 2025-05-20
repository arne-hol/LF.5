import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
x=1
while x<100:
    
    x=random.randint(1,100)
    print(x)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(x/50)
    GPIO.output(16, GPIO.LOW)
    time.sleep(1)
    