# Generated by Django 5.1.4 on 2025-03-21 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_labbotomist_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labbotomist_details',
            old_name='phone_number',
            new_name='mobile_no',
        ),
    ]
