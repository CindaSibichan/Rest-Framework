from rest_framework import serializers
from .models import PersonUser
from .utils import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonUser
        fields = ( 'email', 'password')

    def create(self, validated_data):
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)
    # Extract other fields as needed
        user = PersonUser.objects.create_user(email=email, password=password, **validated_data)
        if PersonUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        user = PersonUser.objects.create_user(email=email, password=password)
    # Additional logic...
        return user
    
class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

