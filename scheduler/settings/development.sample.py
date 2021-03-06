"""Settings to override default settings."""

import logging

#
# Override settings
#
DEBUG = True

HTTP_PORT = 8888
HTTP_ADDRESS = '0.0.0.0'
TIMEZONE = 'Asia/Kolkata'

#
# Set logging level
#
logging.getLogger().setLevel(logging.DEBUG)

JOB_CLASS_PACKAGES = ['scheduler.job_types']

# MySQL Settings
DATABASE_CLASS = 'ndscheduler.core.datastore.providers.mysql.DatastoreMysql'

DATABASE_CONFIG_DICT = {
    'user': 'root',
    'password': '',
    'hostname': '127.0.0.1',
    'port': 3306,
    'database': 'scheduler'
}

AUTHORIZED_EMAILS = []
