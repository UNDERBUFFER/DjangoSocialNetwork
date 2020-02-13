from .serializers import UserSerializer
from admission.backend import Backend
from django.shortcuts import redirect, render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User

class ViewOneObject(APIView):
    serializer_class = UserSerializer
    def get(self, request, iden):
        try:
            obj = UserSerializer(Backend().get_user(iden))
        except:
            pass
        return Response(obj.data)
    def post(self, request, iden):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return redirect('/rest/{}'.format(User.objects.last().id))