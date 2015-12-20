from flask import Flask

from serverpanel.serverinfo import ServerInfo

# Set up Flask App
app = Flask(__name__)

app.config.from_object('config')

server_info = ServerInfo(app)

from serverpanel.controllers import main
from serverpanel.controllers import api

app.register_blueprint(main)
app.register_blueprint(api, url_prefix='/api')
