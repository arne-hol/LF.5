#importieren von Funktionen
import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
x=1
y=1
while x<100:
    x=random.randint(1,100) 
    p =  (99/100)**y
    print(x,y,p*100)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(x/50)
    GPIO.output(16, GPIO.LOW)
    time.sleep(1)
    y +=1
   