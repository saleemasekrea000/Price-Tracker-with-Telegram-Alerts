from celery import Celery

app = Celery("hub_backend")


app = Celery('price_tracker', broker='redis://localhost:6379/0')
