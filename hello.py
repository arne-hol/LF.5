#importieren von Funktionen
import RPi.GPIO as GPIO
import time
import random
#Einstellen der Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
#GPIO.setup(20, GPIO.OUT)
GPIO.setup(6, GPIO.IN)
"""x=1
y=1
while x<100:
    x=random.randint(1,100) 
    p =  (99/100)**y
    print("Random Nummer:",x,"Anzahl der Durchläufe:",y,"Wahrscheinlickeit:",round(p*100,2))
    GPIO.output(16, GPIO.HIGH)
    time.sleep(x/100)
    GPIO.output(16, GPIO.LOW)
    time.sleep(x/100)
    y +=1"""
x = 1
while True:
    if GPIO.input(6) == 1:
        x +=1
        time.sleep(1)
        print(x)
    if x % 2==0:
        #GPIO.output(20, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
       
    else :
        GPIO.output(16, GPIO.HIGH)
        #GPIO.output(20, GPIO.LOW)