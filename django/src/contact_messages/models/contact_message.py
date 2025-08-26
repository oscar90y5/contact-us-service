import os
from django.db import models
import requests


class ContactMessage(models.Model):
    origin = models.CharField(max_length=100)

    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.notify_creation()

        super().save(*args, **kwargs)

    def notify_creation(self):
        message = (f"🥳 ¡Enhorabuena, máquina!\n\n"
                   f"Tienes un nuevo contacto en la página {self.origin}.\n\n"
                   f"📧 Email: {self.email or 'No proporcionado'}\n"
                   f"📞 Teléfono: {self.phone or 'No proporcionado'}\n"
                   f"💬 Mensaje: {self.message}\n")

        requests.post(f"https://api.telegram.org/bot{os.environ.get('TELEGRAM_BOT_TOKEN')}/sendMessage", data={
            "chat_id": os.environ.get('TELEGRAM_CHAT_ID'),
            "text": message
        })
