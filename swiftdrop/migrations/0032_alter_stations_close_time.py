# Generated by Django 3.2.16 on 2023-04-08 05:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('swiftdrop', '0031_auto_20230405_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations',
            name='close_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 8, 10, 54, 58, 269323, tzinfo=utc)),
        ),
    ]
