# Generated by Django 5.1.4 on 2025-03-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0009_coupon_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='price',
        ),
        migrations.AddField(
            model_name='test',
            name='b2b_max_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='b2b_min_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='mrp',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
