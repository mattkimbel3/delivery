# Generated by Django 3.2.16 on 2023-03-29 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swiftdrop', '0002_packaging_packaging_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='packaging',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='swiftdrop.packaging'),
        ),
    ]
