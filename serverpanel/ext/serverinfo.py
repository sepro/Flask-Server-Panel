from datetime import timedelta
from requests import get

import uptime
import psutil
import platform
import math
import socket
import json
import os
import random


class ServerInfo:
    def __init__(self, app=None):
        self.server_type = None

        self.pihole_enabled = False
        self.pihole_api = None

        self.cpu_temp = None

        self.external_network = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['flask-serverinfo'] = self

        self.server_type = platform.system()
        self.pihole_enabled = app.config['ENABLE_PIHOLE'] if 'ENABLE_PIHOLE' in app.config.keys() else False
        self.pihole_api = app.config['PIHOLE_API'] if 'PIHOLE_API' in app.config.keys() else None

        self.cpu_temp = app.config['CPU_TEMP'] if 'CPU_TEMP' in app.config.keys() else None
        self.external_network = app.config['GEOLOCATOR'] if 'GEOLOCATOR' in app.config.keys() else None

        self.testing = app.config['TESTING']

        # these two functions need to be run once to give non-zero output
        psutil.cpu_percent(percpu=True, interval=None)
        self.get_processes()

    @staticmethod
    def get_hostname():
        return socket.gethostname()

    @staticmethod
    def get_os_name():
        return platform.platform()

    @staticmethod
    def get_uptime():
        uptime_seconds = uptime.uptime()
        uptime_str = str(timedelta(seconds=math.floor(uptime_seconds)))

        return uptime_str

    @staticmethod
    def get_cpu_cores():
        data = {'logical_cores': psutil.cpu_count(),
                'physical_cores': psutil.cpu_count(logical=False)
                }

        return data

    @staticmethod
    def get_cpu_load():
        return psutil.cpu_percent(percpu=True, interval=None)

    @staticmethod
    def get_virtual_memory():
        mem = psutil.virtual_memory()._asdict()

        return mem

    @staticmethod
    def get_swap_memory():
        mem = psutil.swap_memory()._asdict()

        return mem

    @staticmethod
    def get_disk_space():
        disk = [{'device': v.device,
                 'mountpoint': v.mountpoint,
                 'fstype': v.fstype,
                 'opts': v.opts,
                 'usage': psutil.disk_usage(v.mountpoint)._asdict()}
                for v in psutil.disk_partitions() if v.fstype != '']

        return disk

    @staticmethod
    def get_disk_io():
        disk_io = [{'device': k,
                    'io': v._asdict()}
                   for k, v in psutil.disk_io_counters(perdisk=True).items()]

        return disk_io

    @staticmethod
    def get_network_io():
        network_config = {}

        for device, values in psutil.net_if_addrs().items():
            for value in values:
                if value.family == socket.AF_INET:
                    network_config[device] = value.address
                    break
            else:
                network_config[device] = 'unknown address'

        network_io = [{'device': k,
                       'io': v._asdict(),
                       'address': network_config[k]}
                      for k, v in psutil.net_io_counters(pernic=True).items()]

        return network_io

    def get_network_external(self):
        output = {}
        try:
            data = get(self.external_network).text
            output = json.loads(data)
        except:
            pass

        if all([a in output.keys() for a in ["ip", "country"]]):
            return output
        else:
            return {'ip': 'Unknown', 'country': 'Unknown'}

    @staticmethod
    def get_processes():
        processes = []

        for proc in psutil.process_iter():
            # Ignore PID 0 (System idle on windows machines)
            if proc.pid != 0:
                processes.append({'pid': proc.pid,
                                  'name': proc.name(),
                                  'cpu_percentage': proc.cpu_percent(interval=None)})

        return sorted(processes, key=lambda k: k['cpu_percentage'], reverse=True)

    def get_temperature(self):
        cpu_temp = random.randint(0, 100) if self.testing else 0

        if os.path.exists(self.cpu_temp):
            with open(self.cpu_temp) as infile:
                cpu_temp = int(infile.read())/1000

        return {'cpu': cpu_temp}

    def get_pihole_stats(self):
        if self.pihole_enabled and self.pihole_api is not None:
            stats = {
                "enabled": self.pihole_enabled,
                "blocked_domains": 0,
                "dns_queries_today": 0,
                "ads_blocked_today": 0,
                "ads_percentage_today": 0,
                "error": False
            }
            try:
                data = json.loads(get(self.pihole_api).text)

                stats = {
                    "enabled": self.pihole_enabled,
                    "blocked_domains": data['domains_being_blocked'],
                    "dns_queries_today": data['dns_queries_today'],
                    "ads_blocked_today": data['ads_blocked_today'],
                    "ads_percentage_today": float(data['ads_percentage_today']),
                    "error": False
                }
            except:
                stats["error"] = True

            return stats
        else:
            return {"enabled": False, "error": False}
