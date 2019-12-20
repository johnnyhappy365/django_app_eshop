from django.db import migrations
from eshop.fixtures import *


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            reset_good_and_category_data_with_created_and_updated,
            roll_back_reset_good_and_category_data_with_created_and_updated,
        )
    ]

