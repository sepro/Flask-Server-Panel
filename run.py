#!/usr/bin/env python3
from serverpanel import create_app

app = create_app('config')

app.run()
