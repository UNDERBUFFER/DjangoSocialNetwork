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

def wall(request, iden):
	if request.GET.get('file', None) is not None:
		return redirect(reverse('photos', args=[iden]))
	if request.GET.get('text', None) is not None:
		return redirect(reverse('records', args=[iden]))
	wall = 'other'
	try:
		obj = User.objects.get(id=request.user.id)
	except:
		obj = None
	if obj is not None:
		if iden == obj.id:
			wall = 'your'
	username = User.objects.get(id=iden).username
	#		if request.POST.get('text', None) not in [None, '']:
	#			Record.objects.create(author=obj, text=request.POST['text'])
	#		if request.FILES.get('file', None) is not None:
	#			Photo.objects.create(author=obj, photo=File(request.FILES['file']))
	if wall == 'your':
		return render(request, 'user/your_wall.html', context={'username': username})
	#	return create_response(request, 'user/your_wall.html', iden)
	return create_response(request, 'user/other_wall.html', context={'username': username})

def photos(request, iden):
	return HttpResponse('maybe photos')

def records(request, iden):
	return HttpResponse('maybe records')