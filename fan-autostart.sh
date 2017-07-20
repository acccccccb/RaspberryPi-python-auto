#!/bin/sh
### BEGIN INIT INFO
# Provides:          fan.sh
# Required-Start:    $network $local_fs $remote_fs $syslog
# Required-Stop::    $network $local_fs $remote_fs $syslog
# Should-Start:      $all
# Should-Stop:       $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: fan to cool down the pi
# Description:       fan to cooldown the pi
### END INIT INFO
#NAME = fan
export HOME="/home/pi"
export USER="root"
#PIDFILE = /home/pi/get.py
echo 'start call py'

python /home/pi/get.py
exit 0
