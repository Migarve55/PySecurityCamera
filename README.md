# PySecurityCamera
Python based security camera.
This project can run in any platform, although it is best suited for a Raspberry Pi.

## Install

```
  sudo pip install Flask
  sudo pip install python-cv2 
```

## Setup

If you want, you can change the default username and password.
Go to the app.py file and change it there.
This is a basic security measure, and I highly recomend you to do it.

## Run

```
  sudo python app.py
```

## Features

  - MJPEG Stream WebServer
  - Security login

## Future features

  - Configuration file
  - Change the configuration on the fly
  - Screenshot saving
  - Pan/Tilt servomotors functionality (Only for RaspberryPi)
