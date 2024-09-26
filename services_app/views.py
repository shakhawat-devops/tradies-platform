
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer
from services_app.permissions import IsOwnerOrReadOnly, IsOwner
from django.contrib.auth import get_user_model

# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer    
    permission_classes = [ permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly ]

    def perform_create(self, serializer):

        serializer.save(service_provider = self.request.user)

