from rest_framework import serializers
from .models import PersonUser
from .utils import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonUser
        fields = ( 'email', 'password')

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        # if PersonUser.objects.filter(email=email).exists():
        #     raise serializers.ValidationError("A user with this email already exists.")
        validated_data.pop('email')
        validated_data.pop('password')

        user = PersonUser.objects.create_user(email, password=password, **validated_data)
        return user
       
class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

