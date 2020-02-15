from rest_framework import serializers
from user.models import Record, User

class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class GetPostRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['text']