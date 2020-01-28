from .functions import access
from django.shortcuts import redirect, render
from django.http import HttpResponse

def chat(request):
    if (res := access(request)) is not True:
        return res
    return render(request, 'chat/chat.html')

def settings(request):
    if (res := access(request)) is not True:
        return res
    return render(request, 'chat/settings.html')