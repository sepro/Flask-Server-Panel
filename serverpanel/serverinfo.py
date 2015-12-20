from subprocess import call, check_output
import platform


class ServerInfo():
    def __init__(self, app=None):
        self.server_type = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
         # register extension with app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['flask-serverinfo'] = self

        self.server_type = app.config['SERVER_TYPE']

    def get_hostname(self):
        hostname = "not found"
        if self.server_type == "WIN":
            hostname = check_output(["hostname"]).decode("utf-8").strip()
        elif self.server_type == "RASPBERRY":
            hostname = check_output(["cat", "/etc/hostname"]).decode("utf-8").strip()

        return hostname

    def get_os_name(self):
        return platform.platform()
