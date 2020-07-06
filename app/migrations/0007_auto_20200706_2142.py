# Generated by Django 3.0.8 on 2020-07-06 19:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200706_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workflow',
            name='parent',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Workflow')),
            ],
        ),
    ]
