from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from accounts import forms
from  django.contrib.auth import login,logout, authenticate

@login_required(login_url="login/")

def home(request):
	return render(request,"home.html")


def register(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form1 = forms.NewUserForm(request.POST)
			if form1.is_valid():
				user = form1.save(commit=False)
				user.save()
				return HttpResponseRedirect('/')
		else:
			form1 = forms.NewUserForm()
		return render(request,'uregister.html',context={
			'form':form1
			})
	else:
		messages.error(request, 'You Are logged In')
		return redirect('/')

def login_user(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/')
        message = 'Invalid email or password'
    return render(request, "login.html", context={'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('/accounts/login')

