from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import PersonUser
from .serializer import UserRegistrationSerializer, OtpVerification
# from .email_utils import send_otp

# Create your views here.
def send_otp(email,otp):
    subject = 'Your OTP Code'
    message = f'Your OTP code is {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

class UserRegistartionView(APIView):
    def post(self , request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            otp = random.randint(100000, 999999)
            user.otp = str(otp)
            user.save()
            send_otp(user.email, otp)
            return Response({"message": "User registered successfully. Check your email for OTP."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

















