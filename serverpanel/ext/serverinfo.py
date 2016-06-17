from datetime import timedelta
from requests import get

import uptime
import psutil
import platform
import math
import socket
import json
import os

class ServerInfo:
    def __init__(self, app=None):
        self.server_type = None

        self.pihole_enabled = False
        self.pihole_blocked_domains = '/etc/pihole/pihole.3.eventHorizon.txt'
        self.pihole_log = '/var/log/pihole.log'

        self.cpu_temp = '/sys/class/thermal/thermal_zone0/temp'

        self.external_network = 'http://ipinfo.io/json'

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['flask-serverinfo'] = self

        self.server_type = platform.system()
        self.pihole_enabled = app.config['ENABLE_PIHOLE'] if 'ENABLE_PIHOLE' in app.config.keys() else False

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
        data = get(self.external_network).text
        return json.loads(data)

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
        cpu_temp = 0
        gpu_temp = 0

        if os.path.exists(self.cpu_temp):
            with open(self.cpu_temp) as infile:
                cpu_temp = int(infile.read())/1000

        return {'cpu': cpu_temp, 'gpu': gpu_temp}

    def get_pihole_stats(self):
        if self.pihole_enabled:
            with open(self.pihole_blocked_domains) as f:
                blocked_domains = sum(1 for line in f)

            with open(self.pihole_log) as f:
                dns_queries_today = sum(1 if 'query' in line else 0 for line in f)

            with open(self.pihole_log) as f:
                ads_blocked_today = sum(1 if '/etc/pihole/gravity.list' in line and 'address' not in line else 0 for line in f)

            ads_percentage_today = (ads_blocked_today * 100.00)/dns_queries_today if dns_queries_today > 0 else 0

            stats = {
                "enabled": self.pihole_enabled,
                "blocked_domains": blocked_domains,
                "dns_queries_today": dns_queries_today,
                "ads_blocked_today": ads_blocked_today,
                "ads_percentage_today": ads_percentage_today
            }

            return stats
        else:
            return {"enabled": False}
