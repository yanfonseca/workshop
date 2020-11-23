from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribeTest(TestCase):

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

    ### Conectar html com o Django 762