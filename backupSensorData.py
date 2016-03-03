#!/usr/bin/env python
import shutil, os, datetime, csv

#get date
#now = datetime.datetime.now().strftime('%Y-%m-%d')
now = 'yesterday'

#store working dir
absWorkingDir = '/home/pi/Desktop/scripts/motion_detector/static/data/'

dataFileName = absWorkingDir + 'pir_state.csv'
archiveFileName = absWorkingDir + now + '.csv'

#copy data
shutil.copy(dataFileName, archiveFileName)

#clear out the old file and rewrite the header
with open(dataFileName, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'state'])

