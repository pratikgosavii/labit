# Generated by Django 5.1.4 on 2025-03-21 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_rename_phone_number_labbotomist_details_mobile_no'),
        ('order', '0004_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='labbotomist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lab.labbotomist_details'),
        ),
    ]
