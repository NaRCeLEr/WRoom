from django.db import models
from django.contrib.auth import get_user_model
from users.models import User

user = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
