from django.urls import path,include
from myapp.views import *




urlpatterns = [
    path('register/',UserRegistrationView.as_view()),
    path('OTP_valid/',OTPVerificationView.as_view()),
    path('login/',UserLoginView.as_view()),
    path('password-reset/', RequestPasswordResetView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
   
]
