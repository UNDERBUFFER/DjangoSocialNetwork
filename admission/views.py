from .forms import RegistrationForm, EntranceForm
#from django.core import signing
from django.shortcuts import redirect, render
from django.urls import reverse
#from hashlib import md5
from user.models import User
from django.contrib.auth import authenticate, login
import time

def registration(request):
	data = {i: request.POST.get(i, None) for i in ['username', 'password', 'email']}
	form = RegistrationForm()
	response = render(request, 'admission/registration.html', context={'form': form})
	if None not in data.values():
		if len(User.objects.filter(email=data['email'])) == 0:
			obj = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
			login(request, obj)
			response = redirect('/user/page/' + str(obj.id))
	return response

def entrance(request):
	data = {i: request.POST.get(i, None) for i in ['password', 'email']}
	form = EntranceForm()
	response = render(request, 'admission/entrance.html', context={'form': form})
	if None not in data.values():
		obj = authenticate(email=data['email'], password=data['password'])
		if obj is not None:
			login(request, obj, backend='admission.backend.Backend')
			response = redirect('/')
	return response

def choice(request):
	if request.GET.get("choice", None) == "registration":
		return redirect(reverse('reg'))
	elif request.GET.get("choice", None) == "entrance":
		return redirect(reverse('ent'))
	else:
		return render(request, 'admission/choice.html')

def start(request):
	if request.user.is_anonymous:
		return redirect('/admission')
	else:
		return redirect('/user/page/' + str(request.user.id))
	#if None in [request.COOKIES.get(i, None) for i in ('user', 'is_authorized')]:
	#	
	#else:
	#	obj = User.objects.get(id=signing.loads(request.COOKIES['user']))
	#	return redirect('/user/page/' + str(obj.id))

#def set_cookie(obj_id):
#	response = redirect('/')
#	response.set_cookie('is_authorized', True)
#	response.set_cookie('user', signing.dumps(obj_id))
#	return response