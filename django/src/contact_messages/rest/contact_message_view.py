from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from contact_messages.models import ContactMessage
from .contact_message_serializer import ContactMessageSerializer


class ContactMessageView(GenericViewSet, CreateModelMixin):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
