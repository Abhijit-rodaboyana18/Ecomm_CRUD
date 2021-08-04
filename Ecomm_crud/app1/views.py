from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignupForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Succesfully')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'signup.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/ecomm_app/home')
        else:
            fm = AuthenticationForm()
        return render(request, 'user_login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


