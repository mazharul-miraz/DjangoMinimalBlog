from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField,AuthenticationForm
from django.contrib.auth.models import User
from more_itertools import strip
from pyrsistent import field

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User 
        fields = ['username', 'first_name','last_name','email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name',
        'email': 'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
}
        
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control', 'autofocus':True})),
    password = forms.CharField(label=("password"), strip=False, widget=forms.PasswordInput(attrs={'class':'form-control', 'autofocus':True, 'autocomplete':'current-password'}))

