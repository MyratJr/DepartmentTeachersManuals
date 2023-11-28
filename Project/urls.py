from django.urls import path
from .views import *

urlpatterns = [
    path('',enter,name='enter'),
    path('video/<int:user_id>/<int:video_id>',videoopen,name='videoopen'),
    path('home',home,name="home"),
    path('maglumat',maglumat,name="maglumat"),
    path('login',loginuser,name="login"),
    path('logout',logoutuser,name="logout"),
]
