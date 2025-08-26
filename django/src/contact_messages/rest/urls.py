from rest_framework.routers import DefaultRouter

from contact_messages.rest.contact_message_view import ContactMessageView


router = DefaultRouter()

router.register(r'contact-messages', ContactMessageView, basename='contact_message')

urlpatterns = router.urls
