from django.test import TestCase

# Create your tests here.

class HomeTest(TestCase):
    
    def test_get(self):
        """GET/Must return status code 200"""
        resp = self.client.get('')
        self.assertEqual(200, resp.status_code )
