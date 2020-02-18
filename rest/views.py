from . import serializers
from admission.backend import Backend
from django.shortcuts import redirect, render
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from user import models
from rest_framework.permissions import AllowAny, IsAuthenticated

class Admission(CreateAPIView):
    serializer_class = serializers.POSTAdmission
    act = None
    def post(self, request, *args, **kwargs):
        if self.act == 'registration':
            data = super().post(request, *args, **kwargs).data
            system = True
        else:
            data = request.data
            system = False
        if (user := Backend().authenticate(email=data['email'], password=data['password'], system=system)) is None:
            return Response()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class User(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.GETUser
    queryset = models.User.objects.all()
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        if kwargs['id'] == request.user.id:
            self.serializer_class = serializers.GETPUTDELETEUser
            response = super().get(request, *args, **kwargs)
            response.data['password'] = ''
            return response
        return super().get(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        if kwargs['id'] == request.user.id:
            self.serializer_class = serializers.GETPUTDELETEUser
            response = super().put(request, *args, **kwargs)
            response.data['password'] = ''
            return response
        return super().get(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        if kwargs['id'] == request.user.id:
            self.serializer_class = serializers.GETPUTDELETEUser
            response = super().delete(request, *args, **kwargs)
            response.data['password'] = ''
            return response 
        return super().get(request, *args, **kwargs)