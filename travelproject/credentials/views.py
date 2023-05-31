from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username=username1,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        user = request.POST['username']
        var1 = request.POST['first_name']
        var = request.POST['last_name']
        var2 = request.POST['email']
        password = request.POST['password']
        cnpassword = request.POST['password1']
        if password==cnpassword:
            if User.objects.filter(username=user).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=var2).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                newvar = User.objects.create_user(username=user,password=password,first_name=var1,last_name=var,email=var2)
                newvar.save()
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')


    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
