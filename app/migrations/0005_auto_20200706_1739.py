# Generated by Django 3.0.8 on 2020-07-06 15:39

from django.db import migrations



class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200706_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='hashed_password',
            new_name='api_key',
        ),
    ]
