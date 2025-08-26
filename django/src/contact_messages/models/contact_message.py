from django.db import models


class ContactMessage(models.Model):
    origin = models.CharField(max_length=100)

    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
