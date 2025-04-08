from rest_framework import serializers
from .  models import Persons

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persons
        fields = '__all__'

    # def validate(self,data):
    #     spc_char = "|@#$%!*()-+?_=,<>/"
    #     if any (c in spc_char for c in data['name']):
    #         raise serializers.ValidationError('Name should not contain special characters')  

    #     return data  
