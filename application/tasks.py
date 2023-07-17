from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


@shared_task
def add(x, y):
    return x + y


@shared_task()
def reminder(message, email):
    html_message = render_to_string("email_template.html", {"message": message})
    send_mail(
        "New reminder",
        "",
        settings.NOREPLY_EMAIL,
        [email],
        fail_silently=False,
        html_message=html_message,
    )
