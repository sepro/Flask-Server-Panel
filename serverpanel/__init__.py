from flask import Flask

from serverpanel.ext.serverinfo import ServerInfo

server_info = ServerInfo()


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    server_info.init_app(app)

    from serverpanel.controllers import main
    from serverpanel.controllers import api

    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    return app
