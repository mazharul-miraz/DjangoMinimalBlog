from django.shortcuts import render
from .form import SignUpForm, LoginForm

# Create your views here.



#home
def home(request):
    return render (request,"home.html")

def about(request):
    return render (request,"about.html")

def contact(request):
    return render (request,"contact.html")

def dashboard(request):
    return render (request,"dashboard.html")

def login(request):
    form = LoginForm()
    return render (request,"login.html",{'form':form} )

def logout(request):
    return render (request,"logout.html")

def signup(request):
    form = SignUpForm()
    return render (request,"signup.html", {'form':form})