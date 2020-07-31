from __future__ import absolute_import, unicode_literals
import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.conf import settings
from celery import shared_task, current_task
import os
import json

@shared_task
def _handle_uploaded_file(files):
    i = 0
    for file in files:
        i = i + 1
        destination = open(os.path.join(settings.BASE_DIR, 'media/{}'.format(file.name)), 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        current_task.update_state(state='PROGRESS',
                                  meta={'current': i, 'total': len(files),
                                        'percent': int((float(i) / len(files)) * 100)})
    return {'current': len(files), 'total': len(files), 'percent': 100}

