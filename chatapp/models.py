from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Room(models.Model):
    room_name = models.CharField(max_length=255)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')

    def __str__(self):
        return self.room_name
    

class ChatRoom(models.Model):
    users = models.ManyToManyField(User, related_name='users')


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return str(self.room)
    

