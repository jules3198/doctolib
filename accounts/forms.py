from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts import models


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = models.CustomUser
		fields = ('username','first_name','last_name','email','role')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,label="username")
    password = forms.CharField(max_length=63,widget=forms.PasswordInput,label="password")
