from django.test import TestCase
from django.core.urlresolvers import reverse


class EcommerceTest(TestCase):
    """Test the ecommerce app"""
    def test_home_page_renders(self):
        url = reverse('home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        # self.assertContains("Welcome to my ecommerce site", resp.content)
