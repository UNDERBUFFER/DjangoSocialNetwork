from django.shortcuts import redirect

def access(request):
	if request.user.is_anonymous:
		return redirect('/')
	return True

def correct_messages(ignores, messages):
	mess = []
	for message in messages:
		bool = True
		for ignore in ignores:
			if ignore.whom == message.author:
				bool = False
		if bool is True:
			mess.append(message)
	return mess