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
	fs=14
	GPIO.setup(fs,GPIO.OUT)
	
	if float(CPU_temp) >= 55 :
		
		print(getCPUtemperature())
		print("Fan power on")
		GPIO.output(fs,GPIO.HIGH)
	
	elif float(CPU_temp) <= 45 :
		GPIO.output(fs,GPIO.LOW)
		print("Fan power off")
		GPIO.cleanup()
	
	else :
		print("CPU Temperature:" + CPU_temp)

	time.sleep(10)
