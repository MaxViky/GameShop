from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from userApp.forms import *


def LogIn(request):
    invalid = 'Invalid login or password'
    if request.method == 'POST':
        form = loginForm(request.POST)
        if 'LogIn' in request.POST:
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect("/")
                    else:
                        return render(request, 'templates/LoginForm.html', {'log_form': form, 'invalid': invalid})
                else:
                    return render(request, 'templates/LoginForm.html', {'log_form': form, 'invalid': invalid})
    else:
        form = loginForm()
    return render(request, 'templates/LoginForm.html', {'log_form': form})


def LogOut(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    if request.method == 'POST':
        user_form = regForms(request.POST)
        if 'regbut' in request.POST:
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password2'])
                new_user.save()
                return redirect("/")
    else:
        user_form = regForms()
    return render(request, 'templates/RegistrationForm.html', {'reg_form': user_form})
