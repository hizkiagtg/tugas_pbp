# Generated by Django 4.1 on 2022-09-22 03:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mywatchlist", "0002_remove_mywatchlist_item_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mywatchlist",
            name="rating",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(1),
                ]
            ),
        ),
    ]