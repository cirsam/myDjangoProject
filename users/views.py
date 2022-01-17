from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    template_name = 'users/index.html'
    return render(request,template_name,{})


def about(request):
    template_name = 'users/aboutus.html'
    return render(request,template_name,{})


