from itertools import count
from string import ascii_letters, digits, punctuation

import requests
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User


def user_create(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")
    username = request.POST.get("username").lower()
    password = str(request.POST.get('password'))

    if username_can_exist(username) and check_password(password) and check_if_email_exists(email):
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)

        ## add checkers
        print(str(user.pk))
        # if not User.objects.filter(user.pk).first():
        user.save()
        return user
    else:
        return None


# else: return None


def user_login(request=requests):
    authenticated_user = User
    if 'log_in_button' in request.POST:
        username_var = request.POST.get("username").lower()
        password_var = str(request.POST.get('password'))
        authenticated_user = authenticate(username=username_var, password=password_var)
    return authenticated_user


def user_logout(request=requests):
    logout(request)

def username_can_exist(username_instance):
    if set(username_instance).difference(ascii_letters + digits) or len(username_instance)<8 or username_instance in User.objects.all():
        return False
    else:
        return True

def check_password(password):
   if set(password).difference(ascii_letters + digits+punctuation) or len(password)<8 :
       return False
   else:
       return True
def check_if_email_exists(email):
    if email in User.objects.all():
        return False
    else:
        return True