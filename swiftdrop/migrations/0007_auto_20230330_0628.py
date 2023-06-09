# Generated by Django 3.2.16 on 2023-03-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiftdrop', '0006_alter_package_package_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='location',
            name='zip_code',
            field=models.IntegerField(default=False),
        ),
    ]
