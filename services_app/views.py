
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer
from .permissions import IsOwnerOrReadOnly, IsOwner
from django.contrib.auth import get_user_model

# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer    
    permission_classes = [IsOwnerOrReadOnly ]

    def perform_create(self, serializer):
        serializer.save(service_provider = self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Service successfully deleted!"}, status=status.HTTP_204_NO_CONTENT)