import json
import requests
from .utils import access_request
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class User(View):
    def get(self, request, *args, **kwargs):
        if not (res := access_request(request, 'http://localhost:8080/user/{}'.format(kwargs['id'])))[0]:
            return render(request, 'user/other_wall.html', context=res[1])
        return render(request, 'user/your_wall.html', context=res[1])
    def put(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

class Photo(View):
    def get(self, request, *args, **kwargs):
        res = access_request(request, 'http://localhost:8080/user/{}/photos'.format(kwargs['author_id']))
        res[1].remove({'Authorization': res[0]})
        context = {'photos': [i[list(i.keys())[0]] for i in res[1] if list(i.keys())[0] != 'Authorization']}
        if not res[0]:
            return render(request, 'user/other_photos.html', context=context)
        return render(request, 'user/your_photos.html', context=context)
    def post(self, request, *args, **kwargs):
        if not (res := access_request(request, 'http://localhost:8080/user/{}/photos'.format(kwargs['author_id'])))[0]:
            return self.get(request, *args, **kwargs)
        if request.FILES.get('photo') is not None:
            requests.post('http://localhost:8080/user/{}/photos'.format(kwargs['author_id']), files={'photo': request.FILES['photo']}, headers={'Authorization': request.COOKIES['Authorization']})
        return self.get(request, *args, **kwargs)

class Record(View):
    def get(self, request, *args, **kwargs):
        res = access_request(request, 'http://localhost:8080/user/{}/records'.format(kwargs['author_id']))
        res[1].remove({'Authorization': res[0]})
        context = {'records': [i[list(i.keys())[0]] for i in res[1] if list(i.keys())[0] != 'Authorization']}
        if not res[0]:
            return render(request, 'user/other_records.html', context=context)
        return render(request, 'user/your_records.html', context=context)
    def post(self, request, *args, **kwargs):
        if not (res := access_request(request, 'http://localhost:8080/user/{}/records'.format(kwargs['author_id'])))[0]:
            return self.get(request, *args, **kwargs)
        if request.POST['text'] != '':
            requests.post('http://localhost:8080/user/{}/records'.format(kwargs['author_id']), data={'text': request.POST['text']}, headers={'Authorization': request.COOKIES['Authorization']})
        return self.get(request, *args, **kwargs)