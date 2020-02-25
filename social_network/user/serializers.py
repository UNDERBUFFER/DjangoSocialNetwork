from rest_framework import serializers
from user.models import *

class GETUser(serializers.ModelSerializer):
    Authorization = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = ['username', 'Authorization']

class GETPUTDELETEUser(serializers.ModelSerializer):
    Authorization = serializers.BooleanField(default=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'Authorization']

class GETPOSTRecord(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['text']

class GETPOSTPhoto(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo']