from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('shopName', 'adress')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('geoPosition', 'skype'),
        }),
    )
admin.site.register(UserProfile, UserProfileAdmin)

