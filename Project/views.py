from django.shortcuts import render
from .forms import Code_getter

def home(request):
    return render(request,"enter.html",{'form':Code_getter})