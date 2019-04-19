from celery import Celery
from app.usgs import ErosWrapper

app = Celery('tasks', broker='redis://redis', backend='redis://redis')


@app.task(name='tasks.locate_scenes')
def locate_scenes(imagery_request_id):
    ErosWrapper.connect()
    return
