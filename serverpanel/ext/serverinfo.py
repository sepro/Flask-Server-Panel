from subprocess import check_output
from datetime import timedelta

import uptime
import psutil
import platform
import math
import socket


class ServerInfo:
    def __init__(self, app=None):
        self.server_type = None
        self.pihole_enabled = False

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

    def get_pihole_stats(self):
        if self.pihole_enabled:
            blocked_domains = int(check_output("wc -l /etc/pihole/pihole.3.eventHorizon.txt | awk '{print $1}'", shell=True))
            dns_queries_today = int(check_output("cat /var/log/pihole.log | awk '/query/ {print $6}' | wc -l", shell=True))
            ads_blocked_today = int(check_output("cat /var/log/pihole.log | awk '/\/etc\/pihole\/gravity.list/ && !/address/ {print $6}' | wc -l", shell=True))
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
