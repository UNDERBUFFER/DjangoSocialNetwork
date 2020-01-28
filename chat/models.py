from django.db import models
from user.models import Record, User

class MyMessageManager(models.Manager):
    def create(self, **kwargs):
        super().create(**kwargs)
        Record.objects.create(**kwargs)

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    objects = MyMessageManager()

class Ignore(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who')
    whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='whom')
