from __future__ import absolute_import
import os
from celery import Celery

#celery -A root worker -l info
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

app = Celery('root')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
