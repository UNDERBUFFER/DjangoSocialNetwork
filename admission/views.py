from .forms import RegistrationForm, EntranceForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.urls import reverse
from user.models import User
from django.contrib.auth import authenticate, login

@user_passes_test(lambda user: True if user.is_anonymous else False, login_url='/')
def registration(request):
	data = {i: request.POST.get(i, None) for i in ['username', 'password', 'email']}
	form = RegistrationForm()
	for i in ['email', 'password', 'username']:
		form.fields[i].widget.attrs["value"] = request.POST.get(i, '')
	response = render(request, 'admission/registration.html', context={'form': form})
	if None not in data.values():
		if len(User.objects.filter(email=data['email'])) == 0:
			obj = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
			login(request, obj)
			response = redirect('/user/wall/' + str(obj.id))
	return response

@user_passes_test(lambda user: True if user.is_anonymous else False, login_url='/')
def entrance(request):
	data = {i: request.POST.get(i, None) for i in ['password', 'email']}
	form = EntranceForm()
	for i in ['email', 'password']:
		form.fields[i].widget.attrs["value"] = request.POST.get(i, '')
	response = render(request, 'admission/entrance.html', context={'form': form})
	if None not in data.values():
		obj = authenticate(email=data['email'], password=data['password'])
		if obj is not None:
			login(request, obj, backend='admission.backend.Backend')
			response = redirect('/')
	return response

@user_passes_test(lambda user: True if user.is_anonymous else False, login_url='/')
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
	return redirect('/user/wall/' + str(request.user.id))

def not_found(request):
	if request.GET.get('return', None) == 'return':
		return redirect('/')
	return render(request, 'admission/not_found.html')