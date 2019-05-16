#!/usr/bin/env python
from flask import Flask, render_template, session, Response, abort, url_for, redirect, request

from camera_opencv import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)
app.secret_key = b'T7fy2T"F4Q8zGHac9Y'

# Settings

user = "admin"
password = "1234"

# Web controls


@app.route('/')
def index():
    if not session['LOGGED']:
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/settings')
def settings():
    if not session['LOGGED']:
        return redirect(url_for('login'))
    return render_template('settings.html')

# Login


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if password == request.args.get('password') and user == request.args.get('username'):
            session['LOGGED'] = True
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def login():
    session['LOGGED'] = False
    return redirect(url_for('login'))

# Camera


@app.route('/feed')
def feed():
    if not session['LOGGED']:
        abort(403)
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
