from django.shortcuts import redirect

def access(request):
	if request.user.is_anonymous:
		return redirect('/')
	return True