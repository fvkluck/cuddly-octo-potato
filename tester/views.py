import logging
import sys
import time

from django.http import HttpResponse
from django.shortcuts import render



logger = logging.getLogger(__name__)

# Create your views here.
def handler(request):
    try:
        logger.error('start')
        while True:
            time.sleep(1)
    except Exception:
        logger.error('exception')
    except BaseException:
        logger.error('baseexception')

    return HttpResponse('hallo')

