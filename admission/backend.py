from django.contrib.auth.backends import BaseBackend
from user.models import User

class Backend(BaseBackend):
	def authenticate(self, request=None, username=None, email=None, password=None):
		if [username, password].count(None) > 1 or email is None:
			return None
		scope = locals()	
		data = {i: eval(i, scope) for i in ['username', 'email', 'password'] if eval(i, scope) is not None}
		try:
			password = data.pop('password')
			user = User.objects.get(**data)
			if not user.check_password(password):
				return None
		except:
			return None
		return user
	def get_user(self, iden):
		return User.objects.get(id=iden)