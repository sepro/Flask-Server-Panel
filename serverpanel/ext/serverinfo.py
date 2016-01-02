from subprocess import check_output
from datetime import timedelta

import uptime
import psutil
import platform


class ServerInfo:
    def __init__(self, app=None):
        self.server_type = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['flask-serverinfo'] = self

        self.server_type = app.config['SERVER_TYPE']

        psutil.cpu_percent(percpu=True, interval=None)

    def get_hostname(self):
        hostname = "not found"
        if self.server_type == "WIN":
            hostname = check_output(["hostname"]).decode("utf-8").strip()
        elif self.server_type == "RASPBERRY":
            with open('/etc/hostname', 'r') as f:
                hostname = f.readline().strip()

        return hostname

    @staticmethod
    def get_os_name():
        return platform.platform()

    def get_uptime(self):
        uptime_seconds = uptime.uptime()
        uptime_str = str(timedelta(seconds=uptime_seconds))

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
