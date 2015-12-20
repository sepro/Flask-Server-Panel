from flask import Blueprint
from serverpanel import server_info

import json

main = Blueprint('main', __name__)
api = Blueprint('api', __name__)


@main.route('/')
def index():
    return 'Hello world'


@api.route('/')
def api_index():
    return json.dumps({'version': '1.0', 'name': 'Flask-Sever-Panel'})


@api.route('/server/hostname')
def api_server_hostname():
    """
    Returns hostname as json object
    :return:
    """
    hostname = server_info.get_hostname()

    return json.dumps({'hostname': hostname})


@api.route('/server/os')
def api_server_os():
    """
    Returns hostname as json object
    :return:
    """
    os_name = server_info.get_os_name()

    return json.dumps({'os_name': os_name})
