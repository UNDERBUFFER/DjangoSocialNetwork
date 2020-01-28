from django.db import models
from user.models import Record, User

class Message(models.Model):
    def __init__(self, **kwargs):
        obj = super(Message, self).__init__(**kwargs)
        Record.objects.create(**kwargs)
        return obj
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

class Ignore(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who')
    whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='whom')
