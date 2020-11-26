from datetime import datetime

from django.test import TestCase
from workshop.subscriptions.models import Subscription


# From here is necessary to think clearly about migrations
# (1) You always have to test with the flag -n
# python manage.py test -n

# (2) You have to migrate first before deployment and to do test with the migrations
# python manage.py makemigrations
# python manage.py migrate

class SubscriptionModelTest(TestCase):
    def test_create_model(self):
        """Model must have name, cpf, email, phone, created_at fields and accept data to be saved"""
        post_example = dict(
            zip(
                ('name', 'cpf', 'email', 'phone'),
                ('John Doe', '12345678901', 'john@email.com', '(61)99999-9999')
            )
        )
        obj = Subscription(**post_example)
        obj.save()

        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Model must have an auto create_at field"""
        post_example = dict(
            zip(
                ('name', 'cpf', 'email', 'phone'),
                ('John Doe', '12345678901', 'john@email.com', '(61)99999-9999')
            )
        )
        obj = Subscription(**post_example)
        obj.save()

        self.assertIsInstance(obj.created_at, datetime)
