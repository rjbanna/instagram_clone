from django import forms
from insta_app.models import *

class LoginForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'

class RegisterForm(forms.Form):
	pass	