import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led=19
fs=26
GPIO.setup(led,GPIO.OUT)
GPIO.setup(fs,GPIO.OUT)
print("I am so cold")
GPIO.output(led,GPIO.LOW)
GPIO.output(fs,GPIO.LOW)
print("fan power off")
GPIO.cleanup()