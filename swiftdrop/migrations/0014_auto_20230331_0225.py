# Generated by Django 3.2.16 on 2023-03-31 09:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('swiftdrop', '0013_auto_20230331_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='stations',
            name='close_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 31, 14, 25, 58, 28491, tzinfo=utc)),
        ),
    ]