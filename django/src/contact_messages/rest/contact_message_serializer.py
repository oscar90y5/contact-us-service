from rest_framework.serializers import ModelSerializer
from ..models import ContactMessage


class ContactMessageSerializer(ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['origin', 'email', 'phone', 'message',]
