from .functions import access
from .models import Message
from django.shortcuts import redirect, render
from django.http import HttpResponse

def chat(request):
    if (res := access(request)) is not True:
        return res
    username = request.user.username
    messages = Message.objects.all().order_by('-id')[:8]
    if request.POST.get('text', None) not in [None, '']:
        Message.objects.create(author=request.user, text=request.POST['text'])
        messages = Message.objects.all().order_by('-id')[:8]
    return render(request, 'chat/chat.html', context={'username': username, 'messages': messages})

def settings(request):
    if (res := access(request)) is not True:
        return res
    return render(request, 'chat/settings.html')