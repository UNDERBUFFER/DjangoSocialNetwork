from .serializers import GetPostRecordSerializer, GetUserSerializer, PostUserSerializer
from admission.backend import Backend
from django.shortcuts import redirect, render
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from user.models import Record, User
from rest_framework.permissions import AllowAny

class PostUser(CreateAPIView):
    serializer_class = PostUserSerializer
    def post(self, request):
        old = super().post(request)
        data = {'detail': 'user is on rest/{}'.format(User.objects.get(email=old.data["email"]).id)}
        return Response(data)

class GetUser(RetrieveUpdateDestroyAPIView):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

class GetPostRecord(ListCreateAPIView):
    serializer_class = GetPostRecordSerializer
    def get(self, request, *args, **kwargs):
        self.queryset = Record.objects.filter(author_id=kwargs['author_id'])
        return super().get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        s = GetPostRecordSerializer(data=request.data)
        if s.is_valid():
            s.save(author=User.objects.get(id=kwargs['author_id']))
        return Response(s.data)

class AuthView(GenericAPIView):
    serializer_class = PostUserSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        user = Backend().authenticate(email=request.data['email'], password=request.data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class Home(GenericAPIView):
    permission_classes = [AllowAny]
    def get(self, request):
        ser = GetUserSerializer(request.user)
        return Response(ser.data)