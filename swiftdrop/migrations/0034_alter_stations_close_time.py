# Generated by Django 3.2.16 on 2023-04-08 06:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('swiftdrop', '0033_auto_20230407_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations',
            name='close_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 8, 11, 0, 53, 141798, tzinfo=utc)),
        ),
    ]
