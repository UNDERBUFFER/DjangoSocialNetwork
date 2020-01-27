from .models import User, Record, Photo
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

def all_walls(request):
	objects = User.objects.all()
	objects = [(i.id, i.username) for i in objects]
	return render(request, 'user/all_walls.html', context={'objects': objects})

#def create_response(request, temp, iden):
#	context = {}
#	context['username'] = User.objects.get(id=iden).username
#	context['records'] = [i.text for i in Record.objects.filter(author=iden)]
#	context['photos'] = [i.photo.name for i in Photo.objects.filter(author=iden)]
#	return render(request, temp, context=context)

def whose(request, iden):
	this = 'other'
	try:
		obj = User.objects.get(id=request.user.id)
	except:
		obj = None
	if obj is not None:
		if iden == obj.id:
			this = 'your'
	return this

def wall(request, iden):
	if request.GET.get('file', None) is not None:
		return redirect(reverse('photos', args=[iden]))
	if request.GET.get('text', None) is not None:
		return redirect(reverse('records', args=[iden]))
	obj = User.objects.get(id=iden)
	username = obj.username
	#		if request.POST.get('text', None) not in [None, '']:
	#			Record.objects.create(author=obj, text=request.POST['text'])
	#		if request.FILES.get('file', None) is not None:
	#			Photo.objects.create(author=obj, photo=File(request.FILES['file']))
	this = whose(request, iden)
	if this == 'your':
		return render(request, 'user/your_wall.html', context={'username': username})
	#	return create_response(request, 'user/your_wall.html', iden)
	return render(request, 'user/other_wall.html', context={'username': username})

def photos(request, iden):
	obj = User.objects.get(id=iden)
	username = obj.username
	photos = [i.photo.name for i in Photo.objects.filter(author=iden)]
	this = whose(request, iden)
	if this == 'your':
		if request.FILES.get('file', None) is not None:
			Photo.objects.create(author=obj, photo=File(request.FILES['file']))
			photos = [i.photo.name for i in Photo.objects.filter(author=iden)]
		return render(request, 'user/your_photos.html', context={'username': username, 'photos': photos})
	#	return create_response(request, 'user/your_wall.html', iden)
	return render(request, 'user/other_photos.html', context={'username': username, 'photos': photos})

def records(request, iden):
	obj = User.objects.get(id=iden)
	username = obj.username
	records = [i.text for i in Record.objects.filter(author=iden)]
	this = whose(request, iden)
	if this == 'your':
		if request.POST.get('text', None) not in [None, '']:
			Record.objects.create(author=obj, text=request.POST['text'])
			records = [i.text for i in Record.objects.filter(author=iden)]
		return render(request, 'user/your_records.html', context={'username': username, 'records': records})
	#	return create_response(request, 'user/your_wall.html', iden)
	return render(request, 'user/other_records.html', context={'username': username, 'recordss': records})