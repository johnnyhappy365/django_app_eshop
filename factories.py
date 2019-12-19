import factory
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()
locale = "zh_CN"


class AdminFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = "eshop_admin"
    "123admin"
    password = "pbkdf2_sha256$180000$eCG6nj48LdI9$jLI8h+FaxKXhSBozZbIfQzTHtbSxaXWNrqecXWlw8/E="
    is_superuser = True
    email = "zhangwy@vip.163.com"
    is_staff = True
    is_active = True


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "User %03d" % n)
    is_superuser: 0


class GoodCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "eshop.GoodCategory"

    name = factory.Faker("company", locale=locale)
    user = factory.SubFactory(AdminFactory)


class GoodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "eshop.Good"

    good_name = factory.Faker("job", locale=locale)
    good_price = 1
    user = factory.SubFactory(AdminFactory)
