from django.urls import path,include
from myapp.views import *




urlpatterns = [
    path('register/',UserRegistrationView.as_view()),


]
