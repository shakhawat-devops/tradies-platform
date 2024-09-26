from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_name', 'email',  'phone_number', 'service_cost', 'description', 'ABN']
        # fields = '__all__'

    # Optionally, you can add custom validation for specific fields
    def validate_service_cost(self, value):
        if value <= 0:
            raise serializers.ValidationError("Service cost must be a positive value.")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
    
        # user_data = {
        #     'id': request.user.get('id'),
        #     'first_name': request.user.get('first_name'),
        #     'last_name': request.user.get('last_name'),
        #     'email': request.user.get('email'),
        # }
        
        validated_data['service_provider'] = request.user.id

        return super().create(validated_data)