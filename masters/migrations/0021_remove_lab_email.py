# Generated by Django 5.1.4 on 2025-03-24 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0020_alter_lab_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='email',
        ),
    ]
