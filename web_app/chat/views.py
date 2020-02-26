import requests
from .utils import access_request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

class Message(View):
    def get(self, request, *args, **kwargs):
        if (res := access_request(request, 'http://localhost:8080/chat/chat')) is False:
            return redirect('http://localhost:8000/admission/entrance')
        return render(request, 'chat/chat.html', context={'data': [{j: i[j] for j in i} for i in res[1]]})
    def post(self, request, *args, **kwargs):
        if (res := access_request(request, 'http://localhost:8080/chat/chat')) is False:
            return self.get(request, *args, **kwargs)
        if request.POST['text'] != '':
            requests.post('http://localhost:8080/chat/chat', data={'text': request.POST['text']}, headers={'Authorization': request.COOKIES['Authorization']})
        return self.get(request, *args, **kwargs)

class Ignore(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request!')
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')