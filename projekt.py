#importieren von Funktionen
import RPi.GPIO as GPIO
import time
import dht11


#Einstellen der Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(18, GPIO.IN)
print(read(dht11.DHT11(18)))

while True:
    #Rot und Weiß
    if GPIO.input(26) == 1:
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
    else:
        GPIO.output(16, GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
    #Blinker
    while GPIO.input(19) == 1:
            GPIO.output(20, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(20, GPIO.LOW)
            time.sleep(0.5)
    while GPIO.input(13) == 1:
            GPIO.output(21, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(21, GPIO.LOW)
            time.sleep(0.5)
    
