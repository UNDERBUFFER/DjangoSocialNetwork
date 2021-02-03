from .serializers import *
from .utils import correct_messages
from chat import models
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user.models import User


class Message(ListCreateAPIView):
    serializer_class = POSTMessage
    queryset = models.Message.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        self.queryset = correct_messages(models.Ignore.objects.filter(
            who=request.user), models.Message.objects.all())[-8:]
        self.serializer_class = GETMessage
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = POSTMessage
        return Response({"text": models.Message.objects.create(text=request.data['text'], author=request.user).text})


class Ignore(ListCreateAPIView):
    serializer_class = GETPOSTIgnore
    queryset = models.Ignore.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        self.queryset = models.Ignore.objects.filter(who=request.user)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            if int(request.data['whom']) != request.user.id:
                if len(models.Ignore.objects.filter(who=request.user, whom=User.objects.get(id=int(request.data['whom'])))) == 0:
                    return Response({"whom": models.Ignore.objects.create(who=request.user, whom=User.objects.get(id=request.data['whom'])).whom.id})
            return Response()
        except:
            return Response()
