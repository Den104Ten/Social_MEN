# Generated by Django 4.2.4 on 2023-09-19 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_post_options_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 19, 15, 44, 54, 160172, tzinfo=datetime.timezone.utc)),
        ),
    ]
