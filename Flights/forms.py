#for Flights
from django import forms

from django.contrib.auth.models import *

from django.contrib.auth.forms import UserCreationForm

from .models import *


class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=120,required=False)
    last_name=forms.CharField(max_length=120,required=False)
    email=forms.EmailField(max_length=200,required=False)

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2',)


    
