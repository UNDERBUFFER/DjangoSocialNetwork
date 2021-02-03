from rest_framework import serializers
from user.models import User


class POSTAdmission(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
