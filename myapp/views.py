from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics
import random
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import PersonUser
from .serializers import *
from .utils import *


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            otp = random.randint(100000, 999999)
            user.otp = str(otp)
            user.save()
            send_otp_email(user.email, otp)
            return Response({"message": "OTP sent successfully. Please verify your email."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

            
class OTPVerificationView(APIView):
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            try:
                user = PersonUser.objects.get(email=email, otp=otp)
                user.otp = None  # Clear the OTP for security reasons
                user.is_active = True  # Mark the user as verified
                user.save()
                
                # Generate JWT tokens for the user
                # refresh = RefreshToken.for_user(user)
                # return Response({
                #     'refresh': str(refresh),
                #     'access': str(refresh.access_token),
                # }, status=status.HTTP_200_OK)
                
                return Response({"message": "User registered successfully."}, status=status.HTTP_200_OK)
            except PersonUser.DoesNotExist:
                return Response({"error": "Invalid OTP or email."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class  UserLoginView(generics.GenericAPIView):

        serializer_class = UserLoginSerializer
        def post(self,request):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data , status=status.HTTP_200_OK)
        


# class RequestPasswordResetEmail(generics.GenericAPIView):
#     serializer_class = ResetPasswordSerializer
#     def post(self , request):



        



















