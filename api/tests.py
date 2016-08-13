from django.test import TestCase
from django.core.urlresolvers import reverse


class APITest(TestCase):
    def setUp(self):
        self.user_data = {'username': 'joe'}

    def tearDown(self):
        self.user_data = None

    def test_user_api_returns_200(self):
        url = reverse('list_create_users')
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)
