from django.db import migrations
from django.contrib.auth.models import User

admin_username = "eshop_admin"
admin_password = "123"


def init_data(apps, schema_editor):
    admin = User.objects.create_superuser(admin_username, admin_password)
    GoodCategory = apps.get_model("eshop", "GoodCategory")
    Good = apps.get_model("eshop", "Good")
    top_cat = GoodCategory.objects.create(name="top", user_id=admin.id)
    food_cat = GoodCategory.objects.create(
        name="food", user_id=admin.id, parent_id=top_cat.id
    )
    phone_cat = GoodCategory.objects.create(
        name="phone", user_id=admin.id, parent_id=top_cat.id
    )

    iphone = Good.objects.create(
        good_name="iphone x",
        good_price=1000,
        category_id=phone_cat.id,
        user_id=1,
    )
    huawei = Good.objects.create(
        good_name="huawei notes",
        good_price=1500,
        category_id=phone_cat.id,
        user_id=1,
    )


def drop_data(apps, schema_editor):
    User.objects.filter(username=admin_username).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0001_initial"),
    ]

    operations = [migrations.RunPython(init_data, drop_data)]

