from flask import Blueprint, render_template, url_for
from serverpanel import server_info
from serverpanel.utils.jsonify import jsonify

main = Blueprint('main', __name__)
api = Blueprint('api', __name__)


@main.route('/')
def index():
    return render_template('main.html')


@api.route('/')
@jsonify
def api_index():
    return {'version': url_for('api.api_version'),
            'server': {
                'hostname': url_for('api.api_server_hostname'),
                'os': url_for('api.api_server_os'),
                'uptime': url_for('api.api_server_uptime')
                },
            'system': {
                'memory': url_for('api.api_system_memory'),
                'swap': url_for('api.api_system_swap'),
                'processes': url_for('api.api_system_processes'),
                'disk_space': url_for('api.api_system_disk_space')
                },
            'network': {
                'io': url_for('api.api_network_io'),
                'external': url_for('api.api_network_external')
            },
            'pihole': {
                'stats': url_for('api.api_pihole_stats')
                }
            }


@api.route('/version')
@jsonify
def api_version():
    return {'version': '1.0', 'name': 'Flask-Sever-Panel'}


@api.route('/server')
@jsonify
def api_server():
    return {'hostname': url_for('api.api_server_hostname'),
            'os': url_for('api.api_server_os'),
            'uptime': url_for('api.api_server_uptime')
            }


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


@api.route('/system/cpu/load')
@jsonify
def api_system_cpu_load():
    return server_info.get_cpu_load()


@api.route('/system/memory')
@jsonify
def api_system_memory():
    return server_info.get_virtual_memory()


@api.route('/system/swap')
@jsonify
def api_system_swap():
    return server_info.get_swap_memory()


@api.route('/system/disk/space')
@jsonify
def api_system_disk_space():
    return server_info.get_disk_space()


@api.route('/system/disk/io')
@jsonify
def api_system_disk_io():
    return server_info.get_disk_io()


@api.route('/system/processes')
@jsonify
def api_system_processes():
    return server_info.get_processes()


@api.route('/system/temp')
@jsonify
def api_system_temp():
    return server_info.get_temperature()


@api.route('/network/io')
@jsonify
def api_network_io():
    return server_info.get_network_io()


@api.route('/network/external')
@jsonify
def api_network_external():
    return server_info.get_network_external()


@api.route('/pihole/stats')
@jsonify
def api_pihole_stats():
    return server_info.get_pihole_stats()
