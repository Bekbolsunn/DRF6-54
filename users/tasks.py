from celery import shared_task
import time
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_otp_email(email, code):
    print("Sending...")
    send_mail(
        "Привет новый пользователь!",
        f"Вот ваш код для подтверждения {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    print("Done")
    return "Ok"

@shared_task
def send_daily_report():
    print("Собираем данные...")
    time.sleep(15)
    print("Успешно")
    return "Ok"
