from django.test import TestCase, Client
from django.urls import reverse
from urllib.parse import urlencode
from .models import Good
import json

client = Client()
# Create your tests here.

  
class GoodTestCase(TestCase):
  def _should_200(self, res):
    self.assertEqual(res.status_code, 200)

  def _should_delete(self, res):
    self.assertEqual(res.status_code, 204)
    
  def test_query_good(self):

    response = client.get(reverse('good_list'))
    self._should_200(response)
    data = json.loads(response.content)
    self.assertEqual(len(data), 0)

  def test_good_detail(self):
    # add test instance
    good = Good.objects.create(good_name='a', good_price=1)

    # test get
    response = client.get(reverse('good_detail', kwargs={ 'pk': good.id }))

    self._should_200(response)
    data = json.loads(response.content)
    self.assertEqual(data['id'], good.id)

    # test update
    response2 = client.put(reverse('good_detail', kwargs={ 'pk': good.id }), data=urlencode({
      'good_name': 'b',
      'good_price': '2'
    }), content_type='application/x-www-form-urlencoded')
    self._should_200(response2)
    data = json.loads(response2.content)
    self.assertEqual(data['good_name'], 'b')

    # test delete
    response3 = client.delete(reverse('good_detail', kwargs={ 'pk': good.id }))
    self._should_delete(response3) 
    