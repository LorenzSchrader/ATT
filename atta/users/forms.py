from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = True) #create field that requires user to input mail.

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
