from django.contrib import admin
from django.contrib.auth.models import Group as UserGroup
from .models import *

admin.site.register(Lecture)
admin.site.register(Degree)
admin.site.register(Department)
admin.site.register(Auditorium)
admin.site.register(Group)
admin.site.unregister(UserGroup)
