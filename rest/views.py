from .serializers import UserSerializer
from admission.backend import Backend
from django.shortcuts import redirect, render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from user.models import User

class ViewOneObject(GenericAPIView):
    serializer_class = UserSerializer
    def get(self, request, iden):
        try:
            obj = UserSerializer(Backend().get_user(iden))
        except:
            return Response('')
        return Response(obj.data)
    def post(self, request, iden):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return redirect('/rest/{}'.format(User.objects.last().id))
    def put(self, request, iden):
        serializer = UserSerializer(instance=Backend().get_user(iden), data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return redirect('/rest/{}'.format(iden))
    def delete(self, request, iden):
        Backend().get_user(iden).delete()
        #return Response('')
        return redirect('/rest/{}'.format(User.objects.last().id))