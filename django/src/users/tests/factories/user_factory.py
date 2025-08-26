import factory
from django.db.models.signals import post_save
from factory import fuzzy
from factory.django import DjangoModelFactory

from ...models.user import User


@factory.django.mute_signals(post_save)
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = fuzzy.FuzzyText(length=20)
