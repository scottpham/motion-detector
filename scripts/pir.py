#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import datetime
import csv

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
formatter = "%H:%M:%S"

#open csv for writing
output_file = open('pir_state.csv', 'w+')
#make a writer object
writer = csv.writer(output_file)

def recordChange(state):
    #record time 
    now = datetime.datetime.now().strftime(formatter)
            
    #log to console
    if state == 1:
        print("there was a change at %s" % (now))
    else:
        print "there was no change at %s" % (now)
   
     #write to csv
    writer.writerow([now, state])
    
    #flush so I can read the file from the system
    output_file.flush()
   

while True:
    #read every second
    time.sleep(1)
    
    #get state
    current_state = GPIO.input(sensor)
   
    #write current_state to a list states
    states.append(current_state)
    
    #log state to the console
    print(current_state)
  
    #if list is 10 items long (set to a minute in production):
    if len(states) >= 10:
        print("Checking 10 second record!")
        #if list contains a 1(true) 
        if states.count(1) >= 1:
            recordChange(1) 
        else:
            recordChange(0)
        #empty list
        states = []
