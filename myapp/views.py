from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import generics
import random
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from restapp.models import Persons
from rest_framework.exceptions import AuthenticationFailed
from .models import PersonUser
from restapp.serializers import *
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .utils import *
from django.urls import reverse


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save(is_active=False)
            otp = random.randint(100000, 999999)
            print(f'Generated OTP: {otp}')
           
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
            otp = str(serializer.validated_data['otp'])
            try:
                user = PersonUser.objects.get(email=email, otp=otp,is_active=False)
                user.otp = str(otp)  
                user.is_active = True  
                user.save()
                
                return Response({"message": "User registered successfully."}, status=status.HTTP_200_OK)
            except PersonUser.DoesNotExist:
                return Response({"error": "Invalid OTP or email."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = authenticate(username=email, password=password)
        
        if not user:
            raise serializers.ValidationError('Invalid credentials')

        if not user.is_active:
            raise serializers.ValidationError('User account is not active')

        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            # 'user': UserLoginSerializer(user).data
        }, status=status.HTTP_200_OK)


# class UserLoginView(generics.GenericAPIView):
#     serializer_class = UserLoginSerializer

#     def post(self , request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data , status=status.HTTP_200_OK)    

# class UserLoginView(APIView):
   

#     def post(self, request):
#         data = request.data
#         serializer = UserLoginSerializer(data=data)
#         if not serializer.is_valid():
#             return Response({"message": serializer.errors, })

#         user_obj = authenticate(
#             username=serializer.data['email'], password=serializer.data['password'])
#         print(" no details:", user_obj)
#         if not user_obj:
#             return Response({"message": "invalid credentials"})

#         try:
#             refresh = RefreshToken.for_user(user_obj)
#             return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'message': 'your data is saved'}, status=status.HTTP_200_OK)
#         except TokenError:
#             return Response({"message": "Access token generation failed. Please try again."}, status=500)

    

# class  UserLoginView(generics.GenericAPIView):

#         serializer_class = UserLoginSerializer
#         def post(self,request):
#             serializer = self.serializer_class(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             return Response(serializer.data , status=status.HTTP_200_OK)
        


# class RequestPasswordResetEmail(generics.GenericAPIView):
#     serializer_class = ResetPasswordSerializer
#     def post(self , request):
#         data ={'request': request , 'data' : request.data}
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response({'sucess' : 'we have sent you a link to reset your password'} , status=status.HTTP_200_OK)

class RequestPasswordResetView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if PersonUser.objects.filter(email=email).exists():
                user = PersonUser.objects.get(email=email)
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = PasswordResetTokenGenerator().make_token(user)
                reset_link = f"{request.scheme}://{request.get_host()}{reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})}"
                send_password_reset(user.email, reset_link)
            return Response({"message": "If your email is registered, you will receive a password reset link."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




        



















