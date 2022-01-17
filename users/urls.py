from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path("", views.index, name="index"),
    path("aboutus/", views.about, name="aboutus"),
]