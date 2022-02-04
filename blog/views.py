from django.shortcuts import render

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
    return render (request,"login.html")

def logout(request):
    return render (request,"logout.html")

def signup(request):
    return render (request,"signup.html")