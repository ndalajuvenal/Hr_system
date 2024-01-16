import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hr_System.settings')
app = Celery('Hr_System')
app.autodiscover_tasks()
@app.task(bin=True, ignore_result = True)
def debug_task(self):
    print(f'Request: {self.request!r}')