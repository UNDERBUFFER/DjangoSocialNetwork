import requests
from .utils import access_request
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View


class Message(View):
    def get(self, request, *args, **kwargs):
        res = access_request(
            request, 'http://{}/chat/chat'.format(settings.REST_API_HOST))
        if res is False:
            return redirect('http://localhost:8000/admission/entrance')
        return render(request, 'chat/chat.html', context={'data': [{j: i[j] for j in i} for i in res[1]]})

    def post(self, request, *args, **kwargs):
        res = access_request(
            request, 'http://{}/chat/chat'.format(settings.REST_API_HOST))
        if res is False:
            return self.get(request, *args, **kwargs)
        if request.POST['text'] != '':
            requests.post('http://{}/chat/chat'.format(settings.REST_API_HOST), data={
                          'text': request.POST['text']}, headers={'Authorization': request.COOKIES['Authorization']})
        return self.get(request, *args, **kwargs)


class Ignore(View):
    def get(self, request, *args, **kwargs):
        res = access_request(
            request, 'http://{}/chat/ignore'.format(settings.REST_API_HOST))
        if res is False:
            return redirect('http://localhost:8000/admission/entrance')
        return render(request, 'chat/ignore.html', context={'ignores': [{j: i[j] for j in i} for i in res[1]]})

    def post(self, request, *args, **kwargs):
        res = access_request(
            request, 'http://{}/chat/ignore'.format(settings.REST_API_HOST))
        if res is False:
            return self.get(request, *args, **kwargs)
        requests.post('http://{}/chat/ignore'.format(settings.REST_API_HOST), data={
                      'whom': request.POST['whom']}, headers={'Authorization': request.COOKIES['Authorization']})
        return self.get(request, *args, **kwargs)
