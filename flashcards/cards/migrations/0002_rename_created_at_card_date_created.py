# Generated by Django 4.1.2 on 2022-11-29 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="card", old_name="created_at", new_name="date_created",
        ),
    ]
