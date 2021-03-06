from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):

    def setUp(self):
        # Use resolve_url and avoid url hardcoded like '/'  /inscricao/
        self.resp = self.client.get(r('home'))

    def test_get(self):
        """GET/Must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must return index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_subscription_link(self):
        """Must contain link to subscriptions in index.html"""
        self.assertContains(self.resp, r('inscricao/'))