# Generated by Django 3.2.16 on 2023-04-02 06:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('swiftdrop', '0021_auto_20230331_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='stations',
            name='close_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 2, 11, 41, 18, 219157, tzinfo=utc)),
        ),
    ]