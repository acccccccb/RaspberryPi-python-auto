import os
import RPi.GPIO as GPIO
import time

count = 0
while ( count == 0 ) :
	# Return CPU temperature as a character string                                     
	def getCPUtemperature():
	    res = os.popen('vcgencmd measure_temp').readline()
	    return(res.replace("temp=","").replace("'C\n",""))
	 
	CPU_temp = getCPUtemperature()
	
	GPIO.setmode(GPIO.BCM)
	led=19
	fs=26
	GPIO.setup(led,GPIO.OUT)
	GPIO.setup(fs,GPIO.OUT)
	
	if float(CPU_temp) >= 55 :
		
		print(getCPUtemperature())
		print("Is too hot")
		GPIO.output(led,GPIO.HIGH)
		GPIO.output(fs,GPIO.HIGH)
	
	elif float(CPU_temp) <= 45 :
		print("I am so cold")
		GPIO.output(led,GPIO.LOW)
		GPIO.output(fs,GPIO.LOW)
		print("fan power off")
		GPIO.cleanup()
	
	else :
		print("so far so good" + CPU_temp)
	
	#count = count + 1
	#print("count=" + str(count))
	time.sleep(30)
