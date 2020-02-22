from rest_framework import serializers
from user.models import *

class POSTAdmission(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class GETUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class GETPUTDELETEUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class GETPOSTRecord(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['text']

class GETPOSTPhoto(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo']