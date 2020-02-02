from django import forms
from user.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'username']
        widgets = {'username': forms.TextInput(attrs={'minlength': 2, 'maxlength': 40, 'placeholder': 'YOUR NAME'}), 'email': forms.EmailInput(attrs={'minlength': 2, 'maxlength': 40, 'placeholder': 'YOUR EMAIL'}), 'password': forms.PasswordInput(attrs={'minlength': 8,  'placeholder': 'YOUR PASSWORD'})}

class EntranceForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {'email': forms.EmailInput(attrs={'minlength': 2, 'maxlength': 40, 'placeholder': 'YOUR EMAIL'}), 'password': forms.PasswordInput(attrs={'minlength': 8,  'placeholder': 'YOUR PASSWORD'})}