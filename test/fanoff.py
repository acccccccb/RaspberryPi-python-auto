import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led=26
fs=14
GPIO.setup(led,GPIO.OUT)
GPIO.setup(fs,GPIO.OUT)
GPIO.output(led,GPIO.LOW)
GPIO.output(fs,GPIO.LOW)
print("fan power off")
GPIO.cleanup()