from . import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user import models

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

class Record(ListCreateAPIView):
    serializer_class = serializers.GETPOSTRecord
    queryset = models.Record.objects.all()
    permission_class = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        self.queryset = models.Record.objects.filter(author_id=kwargs['author_id'])
        return super().get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        if kwargs['author_id'] == request.user.id:
            return Response({"text": models.Record.objects.create(text=request.data['text'], author=request.user).text})
        return super().get(request, *args, **kwargs)

class Photo(ListCreateAPIView):
    serializer_class = serializers.GETPOSTPhoto
    queryset = models.Photo.objects.all()
    permission_class = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        self.queryset = models.Photo.objects.filter(author_id=kwargs['author_id'])
        response = super().get(request, *args, **kwargs)
        data = []
        for i in response.data:
            #data.append({'photo': i['photo'].replace('/photos/mnt/c/Django/social_network/user/static', '')})
            data.append({'photo': i['photo'].replace('/mnt/c/Django/social_network/user/static/user', '')})
            #"http://localhost:8000/user/mnt/c/Django/social_network/user/static/user/1/photos/C30cVgDA5XI.jpg"
            #data.append({'photo': i['photo']})
        response.data = data
        return response
    def post(self, request, *args, **kwargs):
        if kwargs['author_id'] == request.user.id:
            photo =  models.Photo.objects.create(photo=request.data['photo'], author=request.user).photo.name
            photo = photo[photo.rfind('/'):]
            return Response({"photo": request.build_absolute_uri() + photo})
        return super().get(request, *args, **kwargs)