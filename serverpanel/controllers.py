from flask import Blueprint
from serverpanel import server_info
from serverpanel.utils.jsonify import jsonify

main = Blueprint('main', __name__)
api = Blueprint('api', __name__)


@main.route('/')
def index():
    return 'Hello world'


@api.route('/version')
@jsonify
def api_index():
    return {'version': '1.0', 'name': 'Flask-Sever-Panel'}


@api.route('/server/hostname')
@jsonify
def api_server_hostname():
    """
    Returns hostname as json object
    :return:
    """
    hostname = server_info.get_hostname()

    return {'hostname': hostname}


@api.route('/server/os')
@jsonify
def api_server_os():
    """
    Returns operating system as json object
    :return:
    """
    os_name = server_info.get_os_name()

    return {'os_name': os_name}


@api.route('/server/uptime')
@jsonify
def api_server_uptime():
    """
    Returns uptime as json object
    :return:
    """
    uptime = server_info.get_uptime()

    return {'uptime': uptime}


@api.route('/system/cpu/cores')
@jsonify
def api_system_cpu_cores():
    return server_info.get_cpu_cores()


@api.route('/system/disk/space')
@jsonify
def api_system_disk_space():
    return server_info.get_disk_space()


@api.route('/system/disk/io')
@jsonify
def api_system_disk_io():
    return server_info.get_disk_io()
