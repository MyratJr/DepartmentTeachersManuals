from django.contrib import admin
from django.urls import path,re_path,include
from django.views.static import serve as mediaserve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Project.urls')),
    re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                mediaserve, {'document_root': settings.MEDIA_ROOT})
]
