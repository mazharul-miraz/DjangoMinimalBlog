from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .form import SignUpForm, LoginForm

# Create your views here.
from .form import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


#home
def home(request):
    return render (request,"home.html")

def about(request):
    return render (request,"about.html")

def contact(request):
    return render (request,"contact.html")

def dashboard(request):
    return render (request,"dashboard.html")

#Login
def user_login(request):
    if not request.user.is_authenticated: 
        if request.method =="POST":
            form = LoginForm(request=request, data=request.POST or None)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'logged in successfully !!')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render (request,"login.html", {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
    

def logout(request):
    return render (request,"logout.html")


def user_signup(request):
    form = SignUpForm()
    return render (request,"signup.html", {'form':form})