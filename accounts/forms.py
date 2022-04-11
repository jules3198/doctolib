from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts import models


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = models.CustomUser
		fields = ('first_name','last_name','email','role')
