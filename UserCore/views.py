from django.shortcuts import render,redirect
from django.contrib import auth 
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/Guardpass/')
    return render(request,'usercore-pages/login.html',context={})

def sign_up(request):
    if request.method == "POST":
        
        username = request.POST.get('username')
        password =request.POST.get('password')
        if User.objects.filter(username=username).exists():
            print("username is taken")
        else:
            if username and password :
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect("/")
            else:print("Epty fi")


    return render(request,'usercore-pages/signup.html',context={})

