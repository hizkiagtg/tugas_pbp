# Generated by Django 4.1 on 2022-09-22 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mywatchlist", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="mywatchlist", name="item_url",),
    ]
