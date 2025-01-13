from django.urls import path

from . import views

urlpatterns = [
    path("", views.account_view, name="account_view"),
    path("register/", views.account_view_register, name="account_view_register"),
    path("login/", views.account_view_enter, name="account_view_enter"),
    path("logout/", views.account_view_exit, name="account_view_exit"),
]
