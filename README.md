[![Build Status](https://travis-ci.org/sepro/Flask-Server-Panel.svg?branch=master)](https://travis-ci.org/sepro/Flask-Server-Panel) [![codecov.io](https://codecov.io/github/sepro/Flask-Server-Panel/coverage.svg?precision=1)](https://codecov.io/github/sepro/Flask-Server-Panel/)

# Flask-Server-Panel
Server panel based on flask to show stats for a small private server

The back-end is based on Python Flask with a front-end using React.js

![Flask-Server-Panel](./docs/server_panel.png "Server Panel")

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


## Developing the front-end
Install all packages through npm 

    npm install

Build ./serverpanel/static/js/bundle.js using webpack

    webpack -p

