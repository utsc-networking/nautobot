# Generated by Django 3.1.14 on 2021-12-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0007_device_secrets_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='serial',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
