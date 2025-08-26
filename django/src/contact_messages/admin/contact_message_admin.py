from django.contrib import admin

from contact_messages.models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'message', 'created_at',)
    ordering = ('-created_at',)
