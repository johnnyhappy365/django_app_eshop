from django.db import migrations
from django.contrib.auth.models import User
from django.core.management import call_command
from django.conf import settings
from eshop.factories import *

admin_username = "eshop_admin"
admin_password = "123admin"


def init_data(apps, schema_editor):
    if not settings.TESTING:
        # call_command("loaddata", "dev_data")
        admin = AdminFactory()
        top_category = GoodCategoryFactory()
        category1 = GoodCategoryFactory.create(parent=top_category, user=admin)
        category2 = GoodCategoryFactory.create(parent=top_category, user=admin)
        for i in range(10):
            GoodFactory.create(user=admin, category=category1)
            GoodFactory.create(user=admin, category=category2)
    else:
        print("do nothing")
    # admin = User.objects.create_superuser(
    #     admin_username, password=admin_password
    # )
    # GoodCategory = apps.get_model("eshop", "GoodCategory")
    # Good = apps.get_model("eshop", "Good")
    # top_cat = GoodCategory.objects.create(name="top", user_id=admin.id)
    # food_cat = GoodCategory.objects.create(
    #     name="food", user_id=admin.id, parent_id=top_cat.id
    # )
    # phone_cat = GoodCategory.objects.create(
    #     name="phone", user_id=admin.id, parent_id=top_cat.id
    # )

    # iphone = Good.objects.create(
    #     good_name="iphone x",
    #     good_price=1000,
    #     category_id=phone_cat.id,
    #     user_id=admin.id,
    # )
    # huawei = Good.objects.create(
    #     good_name="huawei notes",
    #     good_price=1500,
    #     category_id=phone_cat.id,
    #     user_id=admin.id,
    # )


def drop_data(apps, schema_editor):
    User.objects.filter(username=admin_username).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0001_initial"),
    ]

    operations = [migrations.RunPython(init_data, drop_data)]

