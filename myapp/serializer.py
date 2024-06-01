from rest_framework import serializers
from .models import PersonUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonUser
        fields = ('username', 'email', 'password') 

    def create(self, validated_data):
        user = PersonUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user    
    
class OtpVerification(serializers.Serializer):
    email =  serializers.EmailField()
    otp = serializers.CharField( max_length = 6) 

    

    





