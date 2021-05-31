import signal
import sys

from django.apps import AppConfig

import logging

logger = logging.getLogger(__name__)

def signal_handler(signal_num, frame):
    sys.exit()

class TesterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tester'

    def ready(self):
        logger.error('starting ready')
        signal.signal(signal.SIGTERM, signal_handler)
