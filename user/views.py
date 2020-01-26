from django.core.files import File
from django.shortcuts import render
from .models import User, Record, Photo

def all_walls(request):
	objects = User.objects.all()
	objects = [(i.id, i.username) for i in objects]
	return render(request, 'user/all_walls.html', context={'objects': objects})

def create_response(request, temp, iden):
	context = {}
	context['username'] = User.objects.get(id=iden).username
	context['records'] = [i.text for i in Record.objects.filter(author=iden)]
	context['photos'] = [i.photo.name for i in Photo.objects.filter(author=iden)]
	return render(request, temp, context=context)

def wall(request, iden):
	wall = 'other'
	obj_id = None if request.user.is_anonymous else request.user.id
	obj = User.objects.get(id=obj_id) if obj_id is not None else None
	if obj is not None:
		if iden == obj.id:
			wall = 'your'
			if request.POST.get('about', None) not in [None, '']:
				Record.objects.create(author=obj, text=request.POST['about'])
			if request.FILES.get('file', None) is not None:
				Photo.objects.create(author=obj, photo=File(request.FILES['file']))
	if wall == 'your':
		return create_response(request, 'user/your_wall.html', iden)
	return create_response(request, 'user/other_wall.html', iden)