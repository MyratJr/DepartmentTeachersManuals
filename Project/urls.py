from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('maglumat',maglumat,name="maglumat"),
    path('login',loginuser,name="login"),
    path('logout',logoutuser,name="logout"),
]
