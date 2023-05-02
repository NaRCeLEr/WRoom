from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth import get_user_model

user = get_user_model()


class OrganisationAdmin(UserAdmin):
    admin.site.register(user)
