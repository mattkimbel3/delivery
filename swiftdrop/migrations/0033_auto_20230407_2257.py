# Generated by Django 3.2.16 on 2023-04-08 05:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('swiftdrop', '0032_alter_stations_close_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='delivery_location',
        ),
        migrations.RemoveField(
            model_name='package',
            name='pickup_location',
        ),
        migrations.RemoveField(
            model_name='package',
            name='recipient',
        ),
        migrations.AlterField(
            model_name='stations',
            name='close_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 8, 10, 57, 29, 210456, tzinfo=utc)),
        ),
    ]