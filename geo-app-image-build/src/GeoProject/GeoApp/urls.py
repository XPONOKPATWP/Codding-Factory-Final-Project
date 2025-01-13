from django.urls import path

from . import views

urlpatterns = [
    path("", views.not_logged_in, name="initial_not_logged_in"),
    path("home/", views.home, name="home"),
    path("not_logged_in/", views.not_logged_in, name="not_logged_in"),
    path("map/", views.geo, name="map"),
]
