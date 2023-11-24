from django.contrib.auth import authenticate,logout,login
from django.shortcuts import render, redirect
from .forms import Code_getter

def home(request):
    return render(request,"enter.html",{'form':Code_getter})

def maglumat(request):
    return render(request, "index.html")

def loginuser(request):
    print(1)
    if request.method=='POST':
        print(2)
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print(3)
            login(request, user)
            return redirect('maglumat')
        else: print(4);return redirect('login')
    else: print(5);return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')