from django.test import TestCase
from workshop.subscriptions.forms import SubscriptionForm


# Test object form
class SubscriptionFormTest(TestCase):

    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form must have some fields"""
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(self.form.fields))

# If you want to test form from the page

# from django.test import TestCase
# from django.shortcuts import resolve_url as r
#
# class SubscriptionFormTest(TestCase):
#
#     def setUp(self):
#         self.resp = self.client.get(r('inscricao'))
#
#     def test_form_has_fields(self):
#         """Form must have some fields"""
#         form = self.resp.context['form']
#         self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))
