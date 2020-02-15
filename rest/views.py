from .serializers import CreateSerializer, ViewSerializer
from admission.backend import Backend
from django.shortcuts import redirect, render
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User

class CreateOneObject(CreateAPIView):
    serializer_class = CreateSerializer

class ViewOneObject(RetrieveUpdateDestroyAPIView):
    serializer_class = ViewSerializer
    queryset = User.objects.all()
    lookup_field = 'id'