from django.test import TestCase
from django.shortcuts import resolve_url as r
from workshop.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):

    # Testa a página inscricao e seu form
    def setUp(self):
        # self.resp = self.client.get('/inscricao/')
        self.resp = self.client.get(r('inscricao'))

    def test_get(self):
        """Get /cadastro/ must retunr status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must return subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_htmlpage(self):
        """Must contain input tags in the html"""
        self.assertContains(self.resp, '<form', 1)
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="submit"', 1)
        self.assertContains(self.resp, 'type="email"', 1)

    def test_csrf(self):
        """Must contain csrf in the html"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    # Conectar html e form
    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have some fields"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf','email','phone'], list(form.fields))

