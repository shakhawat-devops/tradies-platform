from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
from services_app import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'services', views.ServiceViewSet, basename="services")


urlpatterns = [
     path('', include(router.urls)),
]