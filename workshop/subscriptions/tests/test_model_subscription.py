from django.test import TestCase
from workshop.subscriptions.models import Subscription

# From here is necessary to think clearly about migrations
# (1) You always have to test with the flag -n or (2) You have to migrate first

# (1)
# python manage.py test -n

# (2)
# python manage.py makemigrations
# python manage.py migrate

class SubscriptionModelTest(TestCase):

    def test_create_model(self):
        post_example = dict(
            zip(
                ('name', 'cpf', 'email', 'phone'),
                ('John Doe', '12345678901', 'john@email.com', '(61)99999-9999')
            )
        )
        obj = Subscription(**post_example)
        obj.save()

        self.assertTrue(Subscription.objects.exists())
