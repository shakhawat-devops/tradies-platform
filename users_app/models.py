from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
# Create your models here.
# from django.core.validators import RegexValidator, EmailValidator
# from django.conf import settings


class User(AbstractBaseUser, PermissionsMixin): 
    email = models.EmailField(max_length=250, unique=True, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)

    objects = UserManager()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [first_name, last_name]

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        full_name = "{} {}".format(self.first_name, self.last_name)
        return full_name


# class Service(models.Model):
#     SERVICE_CATEGORIES = [
#         ('PL', 'Plumbing'),
#         ('EL', 'Electrical'),
#         ('CL', 'Cleaning'),
#         ('CT', 'Construction'),
#         # Add more categories as needed
#     ]
#     service_name = models.CharField(max_length=100, choices=SERVICE_CATEGORIES)
#     email = models.EmailField(validators=[EmailValidator()], max_length=255)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Allows blank but ensures valid format
#     service_cost = models.DecimalField(max_digits=10, decimal_places=2)
#     service_provider = models.ForeignKey( settings.AUTH_USER_MODEL, related_name='services', on_delete=models.CASCADE)
#     description = models.CharField(max_length=1000)

#     ABN = models.CharField(max_length=20)

#     def __str__(self):
#         return self.get_service_name_display()