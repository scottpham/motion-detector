from flask import Flask, render_template, send_file, send_from_directory
import os
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

app = Flask(__name__, static_folder='static')

@app.route('/')
def detectMotion():
    return render_template('motion.html')

#this route just serves the csv for my chart
#@app.route('/data/pir')
#def send_csv():
 #   return send_file('./data/pir_state.csv') 
    
#send archive file
#@app.route('/data/<path:filename>')
#def send_archive(filename):
 #   return send_from_dirctory('../../data/', filename)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

