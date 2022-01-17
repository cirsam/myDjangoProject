from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth

def profile(request):
    template_name = 'accounts/profile.html'
    return render(request,template_name,{})
    
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'accounts/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('accounts:profile')
        else:
            return render(request,'accounts/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('accounts:profile')
        else:
            return render(request,'accounts/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'GET':
        request.session.flush()
        auth.logout(request)
    return redirect('accounts:profile')

