#!/usr/bin/env python
import json
from flask import Flask, render_template, session, Response, abort, url_for, redirect, request

from camera_opencv import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

import piControl

app = Flask(__name__)
app.secret_key = b'T7fy2T"F4Q8zGHac9Y'

# Settings

user = "admin"
password = "1234"

with open('config.json') as configFile:
    config = json.load(configFile)
    user = config["security"]["username"]
    password = config["security"]["username"]

# Web controls


@app.route('/')
def index():
    if not getLogged():
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/settings')
def settings():
    if not getLogged():
        return redirect(url_for('login'))
    return render_template('settings.html')

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
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# Control

@app.route("/servo/<servo>/<action>")
def changeServoPos(servo, action):
    return piControl.changeServoPos(servo, action)

@app.route('/say', methods=['POST'])
def say():
	msg = request.json['msg']
	if msg != None:
		piControl.say(msg)
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
