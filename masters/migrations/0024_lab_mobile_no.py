# Generated by Django 5.1.4 on 2025-03-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0023_remove_test_address_lab_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='mobile_no',
            field=models.CharField(default=1, max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
