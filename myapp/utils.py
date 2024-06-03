from django.core.mail import send_mail
from django.conf import settings
import random
from .models import PersonUser

def send_otp_email(email, otp):
    subject = 'Your OTP Code'
    message = f'Your OTP code is {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    user_obj = PersonUser.objects.get(email = email)
    user_obj.otp = otp
    user_obj.save()


def generate_otp():
    return random.randint(100000, 999999)