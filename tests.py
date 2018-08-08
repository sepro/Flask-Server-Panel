#!/usr/bin/env python3
from serverpanel import create_app
from serverpanel.ext.serverinfo import ServerInfo

from flask_testing import TestCase

import unittest
import json
import unittest.mock as mock
import tempfile
import os

from collections import namedtuple

Request = namedtuple('Request', ['text'])
valid_ip_data = Request(text='{"ip": "127.0.0.1", "country": "BE"}')
valid_pihole_data = Request(text='{"domains_being_blocked": 1,"dns_queries_today":2, '
                                 '"ads_blocked_today": 3, "ads_percentage_today": 50.0}')


class MyTest(TestCase):

    def create_app(self):
        app = create_app('config')
        app.config['DEBUG'] = False

        return app

    def test_creation(self):
        self.app.config['ENABLE_PIHOLE'] = False
        server_info = ServerInfo(self.app)
        self.assertFalse(server_info.pihole_enabled)

        self.app.config['ENABLE_PIHOLE'] = True
        self.app.config['PIHOLE_API'] = None
        server_info = ServerInfo(self.app)
        self.assertTrue(server_info.pihole_enabled)

    def test_main(self):
        # check if route returns code 200
        response = self.client.get('/')
        self.assert_template_used('main.html')
        self.assert200(response)

    def test_api_details(self):
        # check if route returns code 200
        response = self.client.get('/api/version')
        self.assert200(response)
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('name' in data.keys())
        self.assertTrue('version' in data.keys())

    def test_route_hostname(self):
        # check if route returns code 200
        response = self.client.get('/api/server/hostname')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('hostname' in data.keys())

    def test_route_os(self):
        # check if route returns code 200
        response = self.client.get('/api/server/os')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('os_name' in data.keys())

    def test_route_uptime(self):
        # check if route returns code 200
        response = self.client.get('/api/server/uptime')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('uptime' in data.keys())

    def test_route_cpu_cores(self):
        # check if route returns code 200
        response = self.client.get('/api/system/cpu/cores')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('logical_cores' in data.keys())
        self.assertTrue('physical_cores' in data.keys())

    def test_route_cpu_load(self):
        # check if route returns code 200
        response = self.client.get('/api/system/cpu/load')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue(len(data) > 0)

    def test_route_memory(self):
        # check if route returns code 200
        response = self.client.get('/api/system/memory')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('available' in data.keys())
        self.assertTrue('free' in data.keys())
        self.assertTrue('percent' in data.keys())
        self.assertTrue('total' in data.keys())
        self.assertTrue('used' in data.keys())

    def test_route_swap(self):
        # check if route returns code 200
        response = self.client.get('/api/system/swap')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('sin' in data.keys())
        self.assertTrue('sout' in data.keys())
        self.assertTrue('free' in data.keys())
        self.assertTrue('percent' in data.keys())
        self.assertTrue('total' in data.keys())
        self.assertTrue('used' in data.keys())

    def test_route_disk_space(self):
        # check if route returns code 200
        response = self.client.get('/api/system/disk/space')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        for disk in data:
            self.assertTrue('device' in disk.keys())
            self.assertTrue('fstype' in disk.keys())
            self.assertTrue('mountpoint' in disk.keys())
            self.assertTrue('opts' in disk.keys())
            self.assertTrue('usage' in disk.keys())
            self.assertTrue('free' in disk['usage'].keys())
            self.assertTrue('percent' in disk['usage'].keys())
            self.assertTrue('total' in disk['usage'].keys())
            self.assertTrue('used' in disk['usage'].keys())

    def test_route_disk_io(self):
        # check if route returns code 200
        response = self.client.get('/api/system/disk/io')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        for disk in data:
            self.assertTrue('device' in disk.keys())
            self.assertTrue('io' in disk.keys())
            self.assertTrue('read_bytes' in disk['io'].keys())
            self.assertTrue('read_count' in disk['io'].keys())
            self.assertTrue('read_time' in disk['io'].keys())
            self.assertTrue('write_bytes' in disk['io'].keys())
            self.assertTrue('write_count' in disk['io'].keys())
            self.assertTrue('write_time' in disk['io'].keys())

    def test_route_network_io(self):
        # check if route returns code 200
        response = self.client.get('/api/network/io')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        for network in data:
            self.assertTrue('device' in network.keys())
            self.assertTrue('address' in network.keys())
            self.assertTrue('io' in network.keys())
            self.assertTrue('bytes_recv' in network['io'].keys())
            self.assertTrue('bytes_sent' in network['io'].keys())
            self.assertTrue('dropin' in network['io'].keys())
            self.assertTrue('dropout' in network['io'].keys())
            self.assertTrue('errin' in network['io'].keys())
            self.assertTrue('errout' in network['io'].keys())
            self.assertTrue('packets_recv' in network['io'].keys())
            self.assertTrue('packets_sent' in network['io'].keys())

    @mock.patch('serverpanel.ext.serverinfo.get', return_value=valid_ip_data)
    def test_route_network_external_success(self, mocked_get):
        # check if route returns code 200
        response = self.client.get('/api/network/external')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('ip' in data.keys())
        self.assertTrue('country' in data.keys())
        self.assertEqual(data['ip'], '127.0.0.1')
        self.assertEqual(data['country'], 'BE')

    @mock.patch('serverpanel.ext.serverinfo.get', return_value=None)
    def test_route_network_external_fail(self, mocked_get):
        # check if route returns code 200
        response = self.client.get('/api/network/external')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('ip' in data.keys())
        self.assertTrue('country' in data.keys())
        self.assertEqual(data['ip'], 'Unknown')
        self.assertEqual(data['country'], 'Unknown')

    def test_route_temperature_success(self):
        fd, path = tempfile.mkstemp()

        with open(path, "w") as f:
            f.write('100000')

        self.app.extensions['flask-serverinfo'].cpu_temp = path

        # check if route returns code 200
        response = self.client.get('/api/system/temp')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('cpu' in data.keys())
        self.assertEqual(data['cpu'], 100)

        os.close(fd)

    def test_route_temperature_fail(self):
        fd, path = tempfile.mkstemp()

        with open(path, "w") as f:
            f.write('not a number')

        self.app.extensions['flask-serverinfo'].cpu_temp = path

        # check if route returns code 200
        response = self.client.get('/api/system/temp')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('cpu' in data.keys())
        self.assertEqual(data['cpu'], -1)

        os.close(fd)

    def test_route_processes(self):
        # check if route returns code 200
        response = self.client.get('/api/system/processes')
        self.assert200(response)

        # check if object returned contains the desired data
        data = json.loads(response.data.decode('utf-8'))
        for proc in data:
            self.assertTrue('pid' in proc.keys())
            self.assertTrue('name' in proc.keys())
            self.assertTrue('cpu_percentage' in proc.keys())

    def test_pihole_disabled(self):
        self.app.extensions['flask-serverinfo'].pihole_enabled = False
        response = self.client.get('/api/pihole/stats')
        self.assert200(response)

        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('enabled' in data.keys())
        self.assertEqual(data['enabled'], False)
        self.assertEqual(data['error'], False)

    @mock.patch('serverpanel.ext.serverinfo.get', return_value=valid_pihole_data)
    def test_pihole_enabled_success(self, mocked_get):
        self.app.extensions['flask-serverinfo'].pihole_enabled = True
        self.app.extensions['flask-serverinfo'].pihole_api = ''

        response = self.client.get('/api/pihole/stats')
        self.assert200(response)

        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('enabled' in data.keys())
        self.assertEqual(data['error'], False)

    @mock.patch('serverpanel.ext.serverinfo.get', return_value=None)
    def test_pihole_enabled_fail(self, mocked_get):
        self.app.extensions['flask-serverinfo'].pihole_enabled = True
        self.app.extensions['flask-serverinfo'].pihole_api = ''

        response = self.client.get('/api/pihole/stats')
        self.assert200(response)

        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('enabled' in data.keys())
        self.assertEqual(data['error'], True)


if __name__ == '__main__':
    unittest.main()
