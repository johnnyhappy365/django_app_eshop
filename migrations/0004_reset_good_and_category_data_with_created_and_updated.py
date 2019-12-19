from django.db import migrations
from django.contrib.auth.models import User
from django.core.management import call_command
from django.conf import settings
from eshop.fixtures import *
from eshop.factories import admin_username


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0003_auto_20191219_2330"),
    ]

    operations = [
        migrations.RunPython(
            reset_good_and_category_data_with_created_and_updated,
            roll_back_reset_good_and_category_data_with_created_and_updated,
        )
    ]

