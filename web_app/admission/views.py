import json
import requests
from .utils import auth_request
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


def registration(request):
    return auth_request(request, 'http://{}/admission/registration'.format(settings.REST_API_HOST), request.POST, 'admission/registration.html')


def entrance(request):
    return auth_request(request, 'http://{}/admission/entrance'.format(settings.REST_API_HOST), request.POST, 'admission/entrance.html')
