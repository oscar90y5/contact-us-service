from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from users.models import User


class UserAdmin(DjangoUserAdmin):
    list_display = ('username', 'is_staff', 'is_active', 'date_joined',)
    fieldsets = (
        (None, {"fields": ("username", "password", "is_staff", "is_active", "date_joined",)}),
    )
    ordering = ('-date_joined',)

admin.site.register(User, UserAdmin)
