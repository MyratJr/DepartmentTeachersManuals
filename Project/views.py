from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,logout,login
from django.shortcuts import render, redirect
from .forms import Code_getter
from .models import*
from users.models import *

def home(request):
    if request.method=="POST":
        form=Code_getter(request.POST)
        if form.is_valid():
            got=form.cleaned_data['barkod']
            if len(str(got)) == 13:
                try: 
                    teacher=User.objects.select_related("department").prefetch_related('lectures').select_related('degree').get(barkod_san=got)
                except ObjectDoesNotExist:
                    return render(request,'enter.html',{'bellik0':'Mugallym tapylmady, täzeden synanyşyň!','form':Code_getter})
                return render(request,"index.html",{
                    'mugallym':teacher,
                    'videos':Video.objects.filter(property=teacher.id),
                    'manuals':Manual.objects.filter(property=teacher.id),
                    'daily':Daily.objects.filter(property=teacher.id)
                    })
            return render(request,'enter.html',{"bellik0":'Barkod nädogry, täzeden synanyşyň!','form':Code_getter})
        return render(request,'enter.html',{"bellik0":'Nädogry barkod görnüşi, barkodyňyzyň görnüşiniň dogrulygyny anyklaň!',"form":Code_getter})
    return redirect('/')

def enter(request):
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


def videoopen(request,user_id,video_id):
    wideo=Video.objects.filter(property=user_id)
    new_collection_wideo=[]
    one_wideo=[]
    for i in wideo:
        if i.id!=video_id:
            new_collection_wideo.append(i)
        elif i.id==video_id:
            i.view=i.view+1
            i.save()
            one_wideo.append(i)
    return render(request,"video.html",{"video_open":one_wideo,"wideo_open":new_collection_wideo,'mugallym':user_id})