from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1']
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget= forms.PasswordInput())
    