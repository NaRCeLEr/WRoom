from django.db import models
from django.contrib.auth import get_user_model
from users.models import User
from django.utils import timezone
import django

user = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.user}-{self.post}'


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)


class Category(models.Model):
    title = models.CharField(max_length=255)

class Group_Room(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/%Y/%m/%d')
    admins = models.ManyToManyField(User, related_name='admins')
    users = models.ManyToManyField(User, related_name='room_users')
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
