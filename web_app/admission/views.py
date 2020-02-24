import json
import requests
from .utils import auth_request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

def registration(request):
	return auth_request(request, 'http://localhost:8080/admission/registration', request.POST, 'admission/registration.html')

def entrance(request):
	return auth_request(request, 'http://localhost:8080/admission/entrance', request.POST, 'admission/entrance.html')