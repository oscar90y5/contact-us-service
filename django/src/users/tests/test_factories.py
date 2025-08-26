from django.test import TestCase

from .factories import UserFactory
from ..models import User


class TestFactories(TestCase):
    def test_user_factory(self):
        user = UserFactory()
        self.assertIsInstance(user, User)
