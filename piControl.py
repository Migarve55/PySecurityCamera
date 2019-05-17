import RPi.GPIO as GPIO
import time
import pyttsx
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

engine = pyttsx.init()

#Speech
engine.setProperty('voice', 'english')
engine.setProperty('rate', 120)
#Servo pins
servoX = 20
servoY = 21
#Servo positions
servoXpos = 90
servoYpos = 90
#Servos stop
minX = 45
maxX = 135
stepX = 15
minY = 45
maxY = 135
stepY = 15

#Config file
with open('config.json') as configFile:
    config = json.load(configFile)
    #Speech
    engine.setProperty('voice', config["camera"]["speech"]["voice"])
    engine.setProperty('rate',  config["camera"]["speech"]["rate"])
    #Servo pins
    servoX = config["camera"]["servo"]["pan"]["pin"]
    servoY = config["camera"]["servo"]["tilt"]["pin"]
    #Servo positions
    servoXpos = config["camera"]["servo"]["pan"]["pos"]
    servoYpos = config["camera"]["servo"]["tilt"]["pos"]
    #Servos stop
    minX = config["camera"]["servo"]["pan"]["min"]
    maxX = config["camera"]["servo"]["pan"]["max"]
    stepX = config["camera"]["servo"]["pan"]["step"]
    minY = config["camera"]["servo"]["tilt"]["min"]
    maxY = config["camera"]["servo"]["tilt"]["max"]
    stepY = config["camera"]["servo"]["tilt"]["step"]

#Servo declaring
GPIO.setup(servoX, GPIO.OUT)
GPIO.setup(servoY, GPIO.OUT)

   
def constrain(var, min, max):
	if var < min:
		var = min
	elif var > max:
		var = max
	return var


def posToDutyCycle(angle):
	return angle / 18 + 2


def setPinToPos(pin, pos):
    p = GPIO.PWM(pin, 50)  
    p.start(posToDutyCycle(pos))
    time.sleep(0.2)
    p.stop()


def changeServoPos(servo, action):
   global servoXpos
   global servoYpos
   #Get the servo position
   pos = 0
   step = 0
   if servo == "servoX":
       pos = servoXpos
       step = stepX
   elif servo == "servoY":
       pos = servoYpos
       step = stepY
   #Change the servo position
   if action == "left":
       pos += step
   elif action == "right":
       pos -= step
   #Change the servo position
   if servo == "servoX":
       pos = constrain(pos, minX, maxX)
       servoXpos = pos
       setPinToPos(servoX, servoXpos) 
   elif servo == "servoY":
       pos = constrain(pos, minY, maxY)
       servoYpos = pos
       setPinToPos(servoY, servoYpos) 

   return str(pos)


def say(msg):
	engine.say(msg)
	engine.runAndWait()