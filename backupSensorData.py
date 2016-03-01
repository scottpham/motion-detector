#!/usr/bin/env python
import shutil, os, datetime, csv

#get date
#now = datetime.datetime.now().strftime('%Y-%m-%d')
now = 'yesterday'

#store working dir
absWorkingDir = '/home/pi/Desktop/scripts/motion_detector/data'

dataFileName = absWorkingDir + '/pir_state.csv'
archiveFileName = absWorkingDir + '/archive/' + now + '.csv'

#copy data
shutil.copy(dataFileName, archiveFileName)





