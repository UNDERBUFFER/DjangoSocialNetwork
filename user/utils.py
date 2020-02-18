from .models import User

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