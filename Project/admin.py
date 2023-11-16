from django.contrib import messages
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import User, Group as UserGroup
from .models import *

class PropertyImageInline(admin.StackedInline):
    model = Daily

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline ]
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if Daily.objects.count() >= 6:
            messages.error(request,'Cannot add more than 6 Daily objects')
    class Meta:
        model=Teacher

class CustomUserAdmin(UserAdmin):
    list_filter=()
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (('Important dates'), {'fields': ['date_joined']}),
    )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Teacher,PropertyAdmin)
admin.site.register(Lecture)
admin.site.register(Degree)
admin.site.register(Auditorium)
admin.site.register(Group)
admin.site.unregister(UserGroup)