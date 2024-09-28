from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from users_app import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register(r'services', views.ServiceViewSet, basename="services")
router.register(r'users', views.UserViewSet , basename="users")
urlpatterns = [
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view())
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', include(router.urls))
]

# urlpatterns = format_suffix_patterns(urlpatterns)
