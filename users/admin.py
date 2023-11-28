from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class PropertyDailyInline(admin.StackedInline):
    model = Daily


class PropertyVideoInline(admin.StackedInline):
    model = Video


class PropertyManualInline(admin.StackedInline):
    model = Manual
    

def remove_item_from_tuple(original_tuple, item_to_remove):
    new_tuple = []
    for item in original_tuple:
        if item != item_to_remove:
            new_tuple.append(item)

    return new_tuple


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyDailyInline,PropertyVideoInline,PropertyManualInline]
    fieldsets = ()
    fields = (
              'username', 
              'password', 
              'first_name', 
              'last_name', 
              'email', 
              'avatar', 
              'degree', 
              'department', 
              'lectures', 
              'barkod_san', 
              'barkod_surat',
              'is_superuser', 
              'is_staff', 
              'is_active',
              'date_joined',
              
            )
    def get_queryset(self, request):
        if request.user.is_superuser:
            if "user_permissions" not in self.fields:
                self.fields=self.fields+("user_permissions",)
            print(self.fields)
            return super().get_queryset(request)
        if "user_permissions" in self.fields:
            new_tuple=remove_item_from_tuple(self.fields, "user_permissions")
            self.fields=new_tuple
            print(self.fields)
        return super().get_queryset(request).filter(id=request.user.id)
    class Meta:
        model=User


admin.site.register(User, PropertyAdmin)

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):