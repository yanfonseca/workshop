from django.test import TestCase
from django.shortcuts import resolve_url as r
# Create your tests here.

class HomeTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_get(self):
        """GET/Must return status code 200"""
        self.assertEqual(200, self.resp.status_code )

    def test_template(self):
        """Must return index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')