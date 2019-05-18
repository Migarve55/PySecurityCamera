# PySecurityCamera

Python based security camera.
This project can run in any platform, although it is best suited for a Raspberry Pi.
The servo control is only available for the RP platform.

## Install

```
  pip install Flask
  pip install python-cv2 
```

## Setup

If you want, you can change the default username and password.

Use the file "config.json" to change the setup of the program.
Here is an explanation of the config file:

```
  {
    "security": {
        "username": "admin", // Default username CHANGE THIS!!! 
        "password": "1234"   // Default password CHANGE THIS!!!
    },
    "camera": {
        "servo": {
            "pan": {
                "pin": 20,  // GPIO servo pin
                "pos": 90,  // Starting position
                "step": 15, // Step
                "min": 45,  // Min pos
                "max": 135  // Max pos
            },
            "tilt": {
                "pin": 21,  // GPIO servo pin
                "pos": 90,  // Starting position
                "step": 15, // Step
                "min": 45,  // Min pos
                "max": 135  // Max pos
            }
        },
        "speech": {
            "voice": "english", // Language
            "rate": 120         // Speed
        },
        "screenshots": {
            "folder": "screenshots/", // Where to save the screenshots (make sure the folder exists)
            "max": 100                // Max number of saved files
        }
    }
  }
```

## Run

```
  sudo python app.py
```

## Features

  - MJPEG Stream WebServer
  - Security login
  - Pan/Tilt servomotors functionality (Only for RaspberryPi)
  - Text to speech comunication
  - Configuration file
  - Change the configuration on the fly
  - Screenshot saving
