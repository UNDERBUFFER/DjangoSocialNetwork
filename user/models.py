import datetime
import os
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models

class MyUserManager(UserManager):
	def create(self, **kwargs):
		user = super().create(**kwargs)
		user.__setattr__('password', user.password)
		user.save()
		return user
	def get(self, **kwargs):
		if kwargs.get('email', None) is not None:
			return super().get(email=kwargs['email'])
		elif kwargs.get('id', None) is not None:
			return super().get(id=kwargs['id'])
		return None

class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=40)
	email = models.EmailField(max_length=40, unique=True)
	password = models.TextField()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'password']
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	last_login = models.DateTimeField(default=datetime.datetime.now)
	date_joined = models.DateTimeField(default=datetime.datetime.now)
	objects = MyUserManager()
	def __setattr__(self, name, value):
		if name == 'password':
			if not value.startswith('pbkdf2_sha256'):
				value = make_password(value)
		return super().__setattr__(name, value)

class Record(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()

class Photo(models.Model):
	def correct_dir(self, filename):
		return '/mnt/c/Django/social_network/user/static/user/{0}/photos/{1}'.format(self.author.id, filename)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to=correct_dir)