from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from login.models import Audio_store



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']



class AudioForm(forms.ModelForm):
	class Meta:
		model = Audio_store
		fields = ['name', 'record']

		widgets = {
			"name": forms.TextInput(attrs={'class':'form-control', 'id':"exampleInputEmail1", 'aria-describedby':"emailHelp", 'placeholder':"Enter name of the song"})
		}


	