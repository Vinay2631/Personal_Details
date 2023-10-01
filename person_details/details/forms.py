from enum import unique
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Detailsm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:#nested name space will be given
        model=User 
        fields = ['username','email','password1','password2']


        