from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name', 'email', 'is_active', 'is_verified']
