from django.conf import settings
from eshop.factories import *
import random
from datetime import datetime


def random_date():
    day = random.randint(1, 30)
    hour = random.randint(1, 23)
    return datetime.strptime(f"2019-12-{day} {hour}:00:00", "%Y-%m-%d %H:%M:%S")


def reset_good_and_category_data_with_created_and_updated(apps, schema_editor):
    if not settings.TESTING:
        # remove data frist
        User.objects.filter(username=admin_username).delete()

        # init data again
        admin = AdminFactory()
        top_category = GoodCategoryFactory()
        category1 = GoodCategoryFactory.create(parent=top_category, user=admin)
        category2 = GoodCategoryFactory.create(parent=top_category, user=admin)
        for i in range(10):
            f1 = GoodFactory.create(user=admin, category=category1)
            f1.created_at = random_date()
            f1.save()
            f2 = GoodFactory.create(user=admin, category=category2)
            f2.created_at = random_date()
            f2.save()


def roll_back_reset_good_and_category_data_with_created_and_updated(
    apps, schema_editor
):
    User.objects.filter(username=admin_username).delete()
