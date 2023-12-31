import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'periodic_task': {
        'task': 'converter.tasks.get_currencies',
        'schedule': crontab(minute=0, hour=0),
    },
}

