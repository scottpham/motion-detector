#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import datetime
import csv
import os

#connects to middle plug
sensor = 17

#GPIO boilerplate
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

#state vars
previous_state = False
current_state = False

#create empty list
states = []

#date formatter
formatter = "%Y-%m-%d %H:%M:%S"

#yesterday's data
filename = '/home/pi/Desktop/scripts/motion_detector/static/data/pir_state.csv'

#open csv for appending
output_file = open(filename, 'wb')
#make a writer object
writer = csv.writer(output_file)
#write headers
writer.writerow(['time', 'state'])
#close the file
output_file.close()

def recordChange(state):
    #open the file in append mode
    f = open(filename, 'ab')
    #make csv writer
    w = csv.writer(f)    

    #record time 
    now = datetime.datetime.now().strftime(formatter)
            
    #log to console
    if state == 1:
        print("there was a change at %s" % (now))
    else:
        print "there was no change at %s" % (now)
   
    #write to csv
    w.writerow([now, state])
    
    #close so I can read the file from the system
    output_file.close()
   

while True:
    #read every second
    time.sleep(1)
    
    #get state
    current_state = GPIO.input(sensor)
   
    #write current_state to a list states
    states.append(current_state)
    
    #log state to the console
    print(current_state)
  
    #if list is 60 items long log value to csv
    if len(states) >= 60:
        print("Checking 60 second record!")
        #if list contains a 1(true) 
        if states.count(1) >= 1:
            recordChange(1) 
        else:
            recordChange(0)
        #empty list
        states = []
