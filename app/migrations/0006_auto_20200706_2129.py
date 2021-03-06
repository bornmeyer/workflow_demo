# Generated by Django 3.0.8 on 2020-07-06 19:29

import uuid
from django.db import migrations, models


def create_initial_user(apps, schema_editor):
    User = apps.get_model("app", "User")
    new_user = User()
    new_user.email = "test@test.com"
    new_user.firstname = "test"
    new_user.lastname = "test"
    new_user.api_key = uuid.uuid4()
    new_user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200706_1739'),
    ]

    operations = [
        migrations.RunPython(create_initial_user),
    ]
