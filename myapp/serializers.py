from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import PersonUser
from rest_framework_simplejwt.tokens import RefreshToken
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



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)
            print(f"Authenticating with email: {email} and password: {password}")
            if not user:
                print("Authentication failed: Incorrect credentials")
                raise serializers.ValidationError("Incorrect Credentials", code='authorization')

            # Generate JWT tokens for the user
            refresh = RefreshToken.for_user(user)

            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)

        else:
            print("Email or password not provided")

        return attrs



class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ['email']


