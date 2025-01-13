from django import forms
from django.contrib.auth.models import User
from string import ascii_letters,digits

class UserAuthForm(forms.ModelForm):
    username=User.username
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

