import os

DEBUG = False
TESTING = False

ENABLE_PIHOLE = False
PIHOLE_API = 'http://192.168.1.20/admin/api.php'

SECRET_KEY = os.urandom(24)
