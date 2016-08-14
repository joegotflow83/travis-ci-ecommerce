from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework import status

from .serializers import UserSerializer


class APITest(TestCase):
    def setUp(self):
        self.user_data = {'username': 'joe', 'password': 'admin123'}

    def test_user_api_returns_200(self):
        resp = self.client.get(reverse('l_c_users'))
        self.assertEquals(resp.status_code, 200)

    def test_user_api_creation_returns_201(self):
        resp = self.client.post(reverse('l_c_users'), self.user_data)
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)

    def test_single_user_api_returns_200(self):
        user = User.objects.create(username="joe")
        resp = self.client.get(reverse('r_u_d_user', kwargs={'pk': user.pk}))
        self.assertEquals(resp.status_code, 200)

    """def test_put_users_api(self):
        user = User.objects.create(username='joe')
        data = UserSerializer(user).data
        data.update({'username': 'joseph'})
        resp = self.client.put(reverse('r_u_d_user', args=[user.pk]), data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)"""

    def test_destroy_users_api(self):
        user = User.objects.create(username='joe')
        resp = self.client.delete(reverse('r_u_d_user', kwargs=({'pk': user.pk})))
        self.assertEquals(resp.status_code, status.HTTP_204_NO_CONTENT)
