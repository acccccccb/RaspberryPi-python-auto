# RaspberryPi-python-auto

some python for my raspberry pi

> The fan is on GPIO.14

> The LED is on GPIO.26

## 1.clone 

> git clone https://github.com/futureis404/RaspberryPi-python-auto.git

## 2.editor get.py GPIO 

> nano /home/pi/RaspberryPi-python-auto/get.py

## 3.copy fan-autostart.sh to /etc/init.d/ 

> sudo cp /home/pi/RaspberryPi-python-auto/fan-autostart.sh /etc/init.d/fan-autostart

## 4.allow to run fan-autostart


> sudo chmod +x /etc/init.d/fan-autostart

## 5.add service 

> sudo update-rc.d fan-autostart defaults
​
