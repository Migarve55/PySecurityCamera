#!/usr/bin/env python
import json
import datetime
import os
from flask import Flask, render_template, session, Response, abort, url_for, redirect, request

from camera import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

import piControl

app = Flask(__name__)
app.secret_key = b'T7fy2T"F4Q8zGHac9Y'

# Settings

screenshotFolder = "screenshots/"
maxFiles = 100

user = "admin"
password = "1234"

with open('config.json') as configFile:
    config = json.load(configFile)
    screenshotFolder = config["camera"]["screenshots"]["folder"]
    maxFiles = config["camera"]["screenshots"]["maxFiles"]
    user = config["security"]["username"]
    password = config["security"]["password"]

# Web controls

camera = Camera()

@app.route('/')
def index():
    if not getLogged():
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if not getLogged():
        return redirect(url_for('login'))
    if request.method == "GET":
        return render_template('settings.html', con=piControl.getConfig()["camera"])
    elif request.method == "POST":
        newConfig = request.json
        if newConfig == None:
            abort(400)
        piControl.saveNewConfig(newConfig)
        return redirect(url_for('settings'))


# Login


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if password == request.form.get('password') and user == request.form.get('username'):
            session['LOGGED'] = True
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session['LOGGED'] = False
    return redirect(url_for('login'))


# Camera


@app.route('/feed')
def feed():
    if not getLogged():
        abort(403)
    return Response(gen(camera), mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/save')
def save():
    if not getLogged():
        abort(403)
    filename = "screenshot_%s.jpg" % datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    with open(screenshotFolder + filename, "wb") as f:
        frame = camera.get_frame()
        f.write(frame)
        checkFiles()
    return "ok"


@app.route('/centinel/<boolean:mode>')
def setSentinel(mode):
    
    return "ok"


def checkFiles():
    files = sorted(os.listdir(screenshotFolder), key=os.path.getctime)
    if (len(files) > maxFiles):
        oldest = files[0]
        os.remove(screenshotFolder + oldest)


# Control


@app.route("/pos/<servo>")
def getServoPos(servo):
    if not getLogged():
        abort(403)
    return str(piControl.getServoPos(servo))


@app.route("/move/<servo>/<action>")
def changeServoPos(servo, action):
    if not getLogged():
        abort(403)
    return str(piControl.changeServoPos(servo, action))


@app.route('/say', methods=['POST'])
def say():
    if not getLogged():
        abort(403)
    msg = request.json['msg']
    if msg != None:
        piControl.say(msg)
        return "ok"
    else:
        abort(400)

# Auxiliar


def getLogged():
    try:
        return session['LOGGED']
    except:
        return False


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
