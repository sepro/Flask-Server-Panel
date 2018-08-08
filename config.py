import os

DEBUG = False
TESTING = False

ENABLE_PIHOLE = False
PIHOLE_API = 'http://192.168.1.20/admin/api.php'

CPU_TEMP = '/sys/class/thermal/thermal_zone0/temp'
GEOLOCATOR = 'http://ipinfo.io/json'

SECRET_KEY = os.urandom(24)
