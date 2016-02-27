from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y=%m=%d %H:%M")
    templateData = {
        'title' :   'HELLO!',
        'time'  :   timeString
        }
    return render_template('main.html', **templateData)

@app.route("/<pin>/read")
def readPin(pin):
    switch = int(pin)
    try: 
        GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
        if GPIO.input(switch) == True:
            response = "Pin number " + pin + " is high!"
        else:
            response = "Pin number " + pin + " is low!"
    except: 
        response = "There was an error reading pin " + pin + "."
    
    templateData = {
        'title' :   'Status of Pin ' + pin,
        'response': response
    }
    
    return render_template('pin.html', **templateData)

@app.route("/<pin>/<status>")
def turnPinOff(pin, status):
    #store pin as integer variable
    pin = int(pin)
    
    #var for status
    state = ''
    if status == "on":
        state = 1
    elif status == "off":
        state = 0
    else:
        return "Error"
   
    #set up pin as output
    GPIO.setup(pin, GPIO.OUT)
    try:
        #turn pin off
        GPIO.output(pin, state)
        response = "Turned pin number " + str(pin) + " " + status + "."
    except:
        response = "Error accessing pin number " + str(pin) + "."

    templateData = {
        'title'     :   'Turning Off ' + str(pin),
        'status'    :   status,
        'pin'       :   pin,
        'response'  :   response
    }

    return render_template('switch.html', **templateData)

@app.route('/motion')
def detectMotion():
    f = open('scripts/pir_state.txt')
    state = f.readlines()

    templateData = {
     'state'    :   state[0]  
    }

    return render_template('motion.html', **templateData)





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

