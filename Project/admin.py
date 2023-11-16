from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib import admin
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
        model=UserProfile

admin.site.register(UserProfile,PropertyAdmin)
admin.site.register(Lecture)
admin.site.register(Degree)
admin.site.register(Auditorium)
admin.site.register(Group)