from django.test import TestCase
from workshop.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def test_create_model(self):
        post_example = dict(
            zip(
                ('name', 'cpf', 'email', 'phone'),
                ('John Doe', '12345678901', 'john@email.com', '(61)99999-9999')
            )
        )
        obj = Subscription(post_example)
        obj.save()

        self.assertTrue(Subscription.objects.exists())
