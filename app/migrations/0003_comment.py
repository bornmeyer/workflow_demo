# Generated by Django 3.0.8 on 2020-07-06 14:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200706_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Workflow')),
            ],
        ),
    ]
