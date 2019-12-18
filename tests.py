from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from urllib.parse import urlencode
from .models import Good
from datetime import datetime
import json

User = get_user_model()
# Create your tests here.


class GoodTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        username = 'admin'
        password = '123'
        self.admin = User.objects.create(username=username)
        self.admin.set_password(password)
        self.admin.save()

        self.credentials(username, password)

    def credentials(self, username, password):
        response = self._post(reverse('auth'), {
            'username': username,
            'password': password
        })
        self._should_200(response)
        token = json.loads(response.content).get('token')
        self.assertNotEqual(token, None, 'should get token')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def _get(self, path):
        return self.client.get(path)

    def _post(self, path, data):
        return self.client.post(path, data=urlencode(data), content_type='application/x-www-form-urlencoded')

    def _put(self, path, data):
        return self.client.put(path, data=urlencode(data), content_type='application/x-www-form-urlencoded')

    def _delete(self, path):
        return self.client.delete(path)

    def _should_200(self, res):
        self.assertEqual(res.status_code, 200)

    def _should_delete(self, res):
        self.assertEqual(res.status_code, 204)

    def test_query_good(self):

        response = self._get(reverse('good_list'))
        self._should_200(response)
        data = json.loads(response.content)
        self.assertEqual(len(data), 0)

    def test_good_list(self):
        # add two goods for test
        Good.objects.create(good_name='a', good_price=1, user=self.admin)
        Good.objects.create(good_name='b', good_price=2, user=self.admin)

        response = self._get(reverse('good_list'))
        self._should_200(response)

    def test_good_detail(self):
        # add test instance
        good = Good.objects.create(good_name='a', good_price=1, user=self.admin)

        # test get
        response = self._get(
            reverse('good_detail', kwargs={'pk': good.id}))

        self._should_200(response)
        data = json.loads(response.content)
        self.assertEqual(data['id'], good.id)

        response2 = self._put(reverse('good_detail', kwargs={'pk': good.id}), data={
            'good_name': 'b',
            'good_price': '2'
        })

        self._should_200(response2)
        data = json.loads(response2.content)
        self.assertEqual(data['good_name'], 'b')

        # test delete
        response3 = self._delete(
            reverse('good_detail', kwargs={'pk': good.id}))
        self._should_delete(response3)
