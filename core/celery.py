import os
from datetime import timedelta

from celery import Celery

# set the default Django settings module for the "celery" program.
from celery.schedules import crontab  # noqa: I202


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core", broker="amqp://guest@localhost//", backend="rpc://", include=["task"])

app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "send-email-to-admin": {
        "task": "application.tasks.send_mail_to_admin",
        "schedule": crontab(minute="*/10"),
    },
    "parsing": {
        "task": "application.tasks.parse_news",
        "schedule": timedelta(seconds=10),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")  # noqa: T001, T201
