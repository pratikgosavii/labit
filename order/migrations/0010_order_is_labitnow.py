# Generated by Django 5.1.4 on 2025-03-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_labitnow',
            field=models.BooleanField(default=False),
        ),
    ]
