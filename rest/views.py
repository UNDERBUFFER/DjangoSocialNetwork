from .serializers import CreateSerializer, ViewSerializer
from django.shortcuts import redirect, render
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User

class CreateOneObject(CreateAPIView):
    serializer_class = CreateSerializer
    def post(self, request):
        old = super().post(request)
        data = {'detail': 'user is on rest/{}'.format(User.objects.get(email=old.data["email"]).id)}
        return Response(data)

class ViewOneObject(RetrieveUpdateDestroyAPIView):
    serializer_class = ViewSerializer
    queryset = User.objects.all()
    lookup_field = 'id'