from django.db import migrations
from django.contrib.auth.models import User
from django.core.management import call_command
from django.conf import settings
from eshop.fixtures import init_data, drop_init_data
from eshop.factories import admin_username


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0001_initial"),
    ]

    operations = [migrations.RunPython(init_data, drop_init_data)]

