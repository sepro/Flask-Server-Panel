[![Build Status](https://travis-ci.com/sepro/Flask-Server-Panel.svg?branch=master)](https://travis-ci.com/sepro/Flask-Server-Panel) [![codecov.io](https://codecov.io/github/sepro/Flask-Server-Panel/coverage.svg?precision=1)](https://codecov.io/github/sepro/Flask-Server-Panel/)

# Flask-Server-Panel and API

Server panel based on flask to show stats for a small private server. 
Designed specifically with a [Raspberry Pi](https://www.raspberrypi.org/) 
running [Pi-Hole](https://pi-hole.net/) in mind.

The API that is queried by the front-end is located at <your_url>/api/. 
For details check out the [API documentation](./docs/api.md).


The back-end is based on Python [Flask](http://flask.pocoo.org/) with a 
front-end using [React.js](https://facebook.github.io/react/) and 
[Bootstrap](http://getbootstrap.com/)

![Flask-Server-Panel](./docs/server_panel.png "Server Panel")

*Note: The Raspberry Pi logo changes color along with the temperature. 
Green is good, red means you have to invest in a new case with better 
cooling.*

## Getting started

Installation instruction for deployment on a linux system. 

Clone the repository

    git clone https://github.com/sepro/Flask-Server-Panel.git Flask-Server-Panel
    
Set up a virtual environment
    
    cd Flask-Server-Panel
    virtualenv --python=python3 venv
    
Activate the environment and install packages

    source venv/bin/activate
    pip install -r requirements.txt
    
Configure Flask-Server-Panel

    vim config.py

Run tests and run app

    python run_tests.py
    
    python run.py

## Deploy (on x86_64, not rPi!) using Docker

In case you would like to test the panel, a docker container is available. Do note that you will get stats from within the container and not the host system. However, for trying out the app this is the quickest way to get things running.

    docker pull sepro/flask-server-panel
    docker run -p 80:80 -d sepro/flask-server-panel
    
This exposes gunicorn running in the container on port 80 to port 80 on the host system. 

## Developing the front-end
Install all packages through npm 

    npm install

Build ./serverpanel/static/js/bundle.js using webpack

    webpack -p

