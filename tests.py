from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from urllib.parse import urlencode
from .models import Good, GoodCategory
from datetime import datetime
import json

User = get_user_model()
# Create your tests here.


class BaseTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        username = "admin"
        password = "123"
        self._create_user(username, password)
        self._credentials(username, password)

    def _create_user(self, username, password):
        self.admin = User.objects.create(username=username)
        self.admin.set_password(password)
        self.admin.save()

    def _credentials(self, username, password):
        response = self._post(
            reverse("auth"), {"username": username, "password": password}
        )
        self._should_200(response)
        token = json.loads(response.content).get("token")
        self.assertNotEqual(token, None, "should get token")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)

    def _get(self, path, params={}):
        return self.client.get(path, params)

    def _post(self, path, data):
        return self.client.post(
            path,
            data=urlencode(data),
            content_type="application/x-www-form-urlencoded",
        )

    def _put(self, path, data):
        return self.client.put(
            path,
            data=urlencode(data),
            content_type="application/x-www-form-urlencoded",
        )

    def _delete(self, path):
        return self.client.delete(path)

    def _should_200(self, res):
        self.assertEqual(res.status_code, 200)

    def _should_delete(self, res):
        self.assertEqual(res.status_code, 204)


class GoodTestCase(BaseTest):
    def setUp(self):
        super().setUp()

        self.category = GoodCategory.objects.create(
            name="cat1", user=self.admin
        )

    def test_good_list(self):
        response = self._get(reverse("good-list"))
        self._should_200(response)
        data = json.loads(response.content)
        self.assertEqual(len(data["results"]), 2)
        self.assertIsNotNone(data["results"][0]["category"])

    def test_good_filter_by_category(self):
        response = self._get(reverse("good-list"), {"cateogry__name": "phone"})
        self._should_200(response)
        data = json.loads(response.content)
        print("111", data)
        self.assertEqual(data["count"], 2)

    def test_good_list_filter(self):
        # add two goods for test
        Good.objects.create(
            good_name="a", good_price=1, user=self.admin, category=self.category
        )
        Good.objects.create(
            good_name="b", good_price=2, user=self.admin, category=self.category
        )
        Good.objects.create(
            good_name="a", good_price=3, user=self.admin, category=self.category
        )

        # test filter by field
        response = self._get(reverse("good-list"), {"good_name": "a"})
        self._should_200(response)
        data = json.loads(response.content)["results"]
        self.assertEqual(data[0]["good_name"], "a")
        self.assertEqual(
            len(data), 2, "should only return 2 by filter good_name = a"
        )

        # test filter by price
        response = self._get(reverse("good-list"), {"good_price": 2})
        self._should_200(response)
        data = json.loads(response.content)["results"]
        self.assertEqual(data[0]["good_price"], 2)
        self.assertEqual(
            len(data), 1, "should only return 1 by filter good_price = 2"
        )

        # test ordering by id
        response = self._get(reverse("good-list"), {"ordering": "good_price"})
        self._should_200(response)
        data = json.loads(response.content)["results"]
        self.assertEqual(data[0]["good_price"], 1)

        # ordering reverse
        response = self._get(reverse("good-list"), {"ordering": "-good_price"})
        self._should_200(response)
        data = json.loads(response.content)["results"]
        self.assertEqual(data[0]["good_price"], 1500)

        # field and ordering
        response = self._get(
            reverse("good-list"), {"ordering": "-good_price", "good_name": "a"}
        )
        self._should_200(response)
        data = json.loads(response.content)["results"]
        self.assertEqual(data[0]["good_price"], 3)
        self.assertEqual(
            len(data),
            2,
            "should only return 2 by filter good_name = a and ordering = -good_price",
        )

    def test_good_detail(self):
        # add test instance
        good = Good.objects.create(
            good_name="a", good_price=1, user=self.admin, category=self.category
        )

        # test get
        response = self._get(reverse("good-detail", kwargs={"pk": good.id}))

        self._should_200(response)
        data = json.loads(response.content)
        self.assertEqual(data["id"], good.id)

        response2 = self._put(
            reverse("good-detail", kwargs={"pk": good.id}),
            data={"good_name": "b", "good_price": "2"},
        )

        self._should_200(response2)
        data = json.loads(response2.content)
        self.assertEqual(data["good_name"], "b")

        # test delete
        response3 = self._delete(reverse("good-detail", kwargs={"pk": good.id}))
        self._should_delete(response3)


class GoodCategoryTestCase(BaseTest):
    def setUp(self):
        super().setUp()

    def test_good_category_list(self):
        response = self._get(reverse("goodcategory-list"))
        self._should_200(response)
        data = json.loads(response.content)
        self.assertEqual(data["count"], 3)
