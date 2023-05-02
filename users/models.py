from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from .managers import *
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth import get_user_model

class User(AbstractBaseUser, PermissionsMixin):
    image = models.ImageField(null=True, blank=True, upload_to="photos/%Y/%m/%d/")
    friends = models.ManyToManyField('self')
    bio = models.TextField(null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(null=True, blank=True)
    phone = PhoneNumberField(unique=True, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verifed = models.BooleanField(default=False)

    objects = Usermanager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'photo']


