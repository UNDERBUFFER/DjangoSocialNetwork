from .models import *
from rest_framework import serializers

class POSTMessage(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text']

class GETMessage(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'author']

class GETPOSTIgnore(serializers.ModelSerializer):
    class Meta:
        model = Ignore
        fields = ['whom']