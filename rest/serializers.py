from rest_framework import serializers
from user.models import Record, User

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