from cProfile import label
from statistics import mode
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pyrsistent import field

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password(again)',
    widget = forms.PasswordInput())
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'First Name',
                  'email':'Email'}
        