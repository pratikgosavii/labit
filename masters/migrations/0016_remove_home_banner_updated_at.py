# Generated by Django 5.1.4 on 2025-03-21 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0015_home_banner_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home_banner',
            name='updated_at',
        ),
    ]
