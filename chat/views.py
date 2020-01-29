from .functions import access, correct_messages
from .models import Message, Ignore
from django.shortcuts import redirect, render
from django.http import HttpResponse
from user.models import User

def chat(request):
    if (res := access(request)) is not True:
        return res
    who = request.user
    username = who.username
    messages = Message.objects.all()
    if request.POST.get('text', None) not in [None, '']:
        Message.objects.create(author=request.user, text=request.POST['text'])
        messages = Message.objects.all()
    ignores = Ignore.objects.filter(who=who)
    #mess = []
    #for message in messages:
    #    bool = True
    #    for ignore in ignores:
    #        if ignore.whom == message.author:
    #            bool = False
    #    if bool is True:
    #        mess.append(message)
    mess = correct_messages(ignores, messages)[-8:]
    #mess = mess
    return render(request, 'chat/chat.html', context={'username': username, 'messages': mess})

def settings(request):
    if (res := access(request)) is not True:
        return res
        
    if request.POST.get('whom', None) not in [None, '']:
        who = request.user
        whom = User.objects.get(id=request.POST['whom'])
        if who.id == whom.id:
            pass
        elif len(Ignore.objects.filter(who=who, whom=whom)) != 0:
            pass
        else:
            Ignore.objects.create(who=who, whom=whom)
    return render(request, 'chat/settings.html')