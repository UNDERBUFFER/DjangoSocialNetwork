from rest_framework import serializers
from user.models import User

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']