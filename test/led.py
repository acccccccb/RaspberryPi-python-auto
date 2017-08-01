import RPi.GPIO as GPIO
import time

LED = 26
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

while ( count < 3 ) :
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)
    count = count + 1

print("Service already started")
GPIO.cleanup()