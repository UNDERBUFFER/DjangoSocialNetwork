from .models import Message, Ignore
from .utils import correct_messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.http import HttpResponse
from user.models import User

@user_passes_test(lambda user: False if user.is_anonymous else True, login_url='/')
def chat(request):
    who = request.user
    messages = Message.objects.all()
    if request.POST.get('text', None) not in [None, '']:
        Message.objects.create(author=request.user, text=request.POST['text'])
        messages = Message.objects.all()
    ignores = Ignore.objects.filter(who=who)
    mess = correct_messages(ignores, messages)[-8:]
    return render(request, 'chat/chat.html', context={'username': who.username, 'messages': mess})

@user_passes_test(lambda user: False if user.is_anonymous else True, login_url='/')
def settings(request):
    who = request.user
    if request.POST.get('whom', None) not in [None, '']:
        whom = User.objects.get(id=request.POST['whom'])
        if who.id == whom.id:
            pass
        elif len(Ignore.objects.filter(who=who, whom=whom)) != 0:
            pass
        else:
            Ignore.objects.create(who=who, whom=whom)
    ignores = Ignore.objects.filter(who=who)
    return render(request, 'chat/settings.html', context={'username': who.username, 'ignores': ignores})