from flask import Blueprint
from serverpanel import server_info

import json

main = Blueprint('main', __name__)
api = Blueprint('api', __name__)


@main.route('/')
def index():
    return 'Hello world'


@api.route('/version')
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
    Returns operating system as json object
    :return:
    """
    os_name = server_info.get_os_name()

    return json.dumps({'os_name': os_name})


@api.route('/server/uptime')
def api_server_uptime():
    """
    Returns uptime as json object
    :return:
    """
    uptime = server_info.get_uptime()

    return json.dumps({'uptime': uptime})


@api.route('/system/cpu/cores')
def api_system_cpu_cores():
    return json.dumps(server_info.get_cpu_cores())


@api.route('/system/disk/space')
def api_system_disk_space():
    return json.dumps(server_info.get_disk_space())
