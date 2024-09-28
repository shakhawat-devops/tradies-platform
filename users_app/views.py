from django.shortcuts import render
from users_app.serializers import UserSerializer
from rest_framework import generics, viewsets, permissions
# from django.contrib.auth.models import User
# from .models import Service
# from .serializers import ServiceSerializer
from django.contrib.auth import get_user_model
# from users_app.permissions import IsOwnerOrReadOnly, IsOwner
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
User = get_user_model()
from .permissions import IsOwner

# Create your views here.
class RegisterView(generics.CreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomTokenVerifyView(TokenVerifyView):
     def post(self, request, *args, **kwargs):
        # Call the default token verification logic
        serializer = TokenVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Extract the user ID from the valid token
        token = AccessToken(request.data['token'])
        user_id = token['user_id']
        
        # Get the user object and send back the relevant data
        user = User.objects.get(id=user_id)
        user_data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_authenticated': True
        }

        return Response({
            'token_valid': True,
            'user': user_data
        })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =  [permissions.IsAuthenticated, IsOwner]
    def get_queryset(self):
        # Ensure that the user can only see their own profile
        return User.objects.filter(id=self.request.user.id)

    def perform_update(self, serializer):
        # Ensure that users can only update their own profile
        serializer.save(user=self.request.user)


# class ServiceViewSet(viewsets.ModelViewSet):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer    
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly ]

#     def perform_create(self, serializer):
#         # Set the user as the service provider
#         serializer.save(service_provider=self.request.user)