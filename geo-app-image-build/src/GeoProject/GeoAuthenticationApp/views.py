import string

from django.contrib.sites import requests
from django.shortcuts import render, redirect

from GeoApp.views import not_logged_in, home
from GeoAuthenticationApp.forms import UserAuthForm
from GeoAuthenticationApp.scripts.user_manage import user_login, user_logout, user_create


# Create your views here.
def account_view(request=requests):
    curr_se = request.session
    curr_user = curr_se.get("user") or None
    if curr_user is None:
        return redirect(account_view_register)
    else:
        return redirect(account_view_enter)


def account_view_register(request):
    html_page = "registration/user_registration.html"
    user_form = UserAuthForm
    essential_character={
        "ascii_letters":string.ascii_letters,
        "digits":string.digits,
        "punc":string.punctuation
    }
    context = {
        "user_form": user_form,
        "essential":essential_character
    }
    if request.method == 'POST':
        if 'sign_up_button' in request.POST:
            user = user_create(request)
            if user is not None:
                return redirect(not_logged_in)
            else:
                return redirect(account_view_register)
        if 'already_login_button' in request.POST:
            return redirect(account_view_enter)
    else:
        return render(request, html_page, context)


def account_view_enter(request=requests):
    user_form = UserAuthForm
    html_page = "registration/user_login.html"
    if 'log_in_button' in request.POST:
        curr_user = user_login(request)
        if curr_user is not None and curr_user.is_authenticated:
            request.session['user'] = {
                "username": curr_user.username,
                "is_authenticated": curr_user.is_authenticated
            }
            return redirect(home)
        else:
            return redirect(account_view_enter)
    if 'want_to_register_button' in request.POST:
        return redirect(account_view_register)
    context = {
        "user_form": user_form,
        "request": request.POST,
    }
    return render(request, html_page, context)


def account_view_exit(request):
    user_logout(request)
    return redirect(account_view_register)
