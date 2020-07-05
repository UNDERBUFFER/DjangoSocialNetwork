from .serializers import *
from django.conf import settings
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user import models

class User(RetrieveUpdateDestroyAPIView):
    serializer_class = GETUser
    queryset = models.User.objects.all()
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        if kwargs['id'] == request.user.id:
            self.serializer_class = GETPUTDELETEUser
            response = super().get(request, *args, **kwargs)
            response.data['password'] = ''
            return response
        return super().get(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        if kwargs['id'] == request.user.id:
            self.serializer_class = GETPUTDELETEUser
            response = super().put(request, *args, **kwargs)
            response.data['password'] = ''
            return response
        return super().get(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        if kwargs['id'] == request.user.id:
            self.serializer_class = GETPUTDELETEUser
            response = super().delete(request, *args, **kwargs)
            response.data['password'] = ''
            return response 
        return super().get(request, *args, **kwargs)

class Record(ListCreateAPIView):
    serializer_class = GETPOSTRecord
    queryset = models.Record.objects.all()
    permission_class = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        self.queryset = models.Record.objects.filter(author_id=kwargs['author_id'])
        response = super().get(request, *args, **kwargs)
        response.data.append({'Authorization': True if kwargs['author_id'] == request.user.id else False})
        return response
    def post(self, request, *args, **kwargs):
        if kwargs['author_id'] == request.user.id:
            return Response([{"text": models.Record.objects.create(text=request.data['text'], author=request.user).text}, {'Authorization': True}])
        response = super().get(request, *args, **kwargs)
        response.data.append({'Authorization': False})
        return response

class Photo(ListCreateAPIView):
    serializer_class = GETPOSTPhoto
    queryset = models.Photo.objects.all()
    permission_class = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        self.queryset = models.Photo.objects.filter(author_id=kwargs['author_id'])
        response = super().get(request, *args, **kwargs)
        data = []
        for i in response.data:
            data.append({'photo': i['photo'].replace(settings.MEDIA_ROOT[:-1], '')})
        response.data = data
        response.data.append({'Authorization': True if kwargs['author_id'] == request.user.id else False})
        return response
    def post(self, request, *args, **kwargs):
        if kwargs['author_id'] == request.user.id:
            photo =  models.Photo.objects.create(photo=request.data['photo'], author=request.user).photo.name
            photo = photo[photo.rfind('/'):]
            return Response([{"photo": request.build_absolute_uri() + photo}, {'Authorization': True}])
        response = super().get(request, *args, **kwargs)
        response.data.append({'Authorization': False})
        return response