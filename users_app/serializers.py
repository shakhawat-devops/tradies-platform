from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        max_length=255,
        validators=[UniqueValidator(queryset=User.objects.all())],
        allow_blank = False
    )

    class Meta: 
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'password']
        exargs = {'password': {'write_only': True}}


    def create(self, data):
        # user = User.objects.create_user(**validated_data)
        user = User.objects.create_user(**data)
        return user

    
    
# class ServiceSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Service
    #     fields = ['id', 'service_name', 'email', 'phone_number', 'service_cost', 'description']

    # # Optionally, you can add custom validation for specific fields
    # def validate_service_cost(self, value):
    #     if value <= 0:
    #         raise serializers.ValidationError("Service cost must be a positive value.")
    #     return value

    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     validated_data['service_provider'] = request.user  # Assign the logged-in user to the service
    #     return super().create(validated_data)