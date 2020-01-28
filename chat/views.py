from django.shortcuts import render
from django.http import HttpResponse

def process(request):
    return HttpResponse('ok')