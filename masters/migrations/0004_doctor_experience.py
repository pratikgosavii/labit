# Generated by Django 5.1.4 on 2025-03-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0003_alter_doctor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
