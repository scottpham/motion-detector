#!/usr/bin/env bash


nohup python -u /home/pi/Desktop/scripts/motion_detector/runSensor.py &

SENSORPID=`echo $!`

exit 0
